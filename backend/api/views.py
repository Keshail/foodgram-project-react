from urllib.parse import unquote

from django.contrib.auth import get_user_model
from django.db.models import F, Sum
from django.http.response import HttpResponse
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet as DjoserUserViewSet
from recipes.models import AmountIngredient, Ingredient, Recipe, Tag
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import conf
from .mixins import AddDelViewMixin
from .paginators import PageLimitPagination
from .permissions import AdminOrReadOnly, AuthorStaffOrReadOnly
from .serializers import (IngredientSerializer, RecipeSerializer,
                          ShortRecipeSerializer, TagSerializer,
                          UserSubscribeSerializer)
from .services import incorrect_layout

User = get_user_model()


class UserViewSet(DjoserUserViewSet, AddDelViewMixin):
    pagination_class = PageLimitPagination
    add_serializer = UserSubscribeSerializer

    @action(methods=conf.ACTION_METHODS, detail=True)
    def subscribe(self, request, id):
        return self.add_del_obj(id, conf.SUBSCRIBE_M2M)

    @action(methods=('get',), detail=False)
    def subscriptions(self, request):
        user = self.request.user
        if user.is_anonymous:
            return Response(status=HTTP_401_UNAUTHORIZED)
        authors = user.subscribe.all()
        pages = self.paginate_queryset(authors)
        serializer = UserSubscribeSerializer(
            pages, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AdminOrReadOnly,)


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        name = self.request.query_params.get(conf.SEARCH_ING_NAME)
        queryset = self.queryset
        if name:
            if name[0] == '%':
                name = unquote(name)
            else:
                name = name.translate(incorrect_layout)
            name = name.lower()
            stw_queryset = list(queryset.filter(name__startswith=name))
            cnt_queryset = queryset.filter(name__contains=name)
            stw_queryset.extend(
                [i for i in cnt_queryset if i not in stw_queryset]
            )
            queryset = stw_queryset
        return queryset


class RecipeViewSet(ModelViewSet, AddDelViewMixin):
    queryset = Recipe.objects.select_related('author')
    serializer_class = RecipeSerializer
    permission_classes = (AuthorStaffOrReadOnly,)
    pagination_class = PageLimitPagination
    add_serializer = ShortRecipeSerializer
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        queryset = self.queryset

        tags = self.request.query_params.getlist(conf.TAGS)
        if tags:
            queryset = queryset.filter(
                tags__slug__in=tags).distinct()

        author = self.request.query_params.get(conf.AUTHOR)
        if author:
            queryset = queryset.filter(author=author)

        user = self.request.user
        if user.is_anonymous:
            return queryset

        is_in_shopping = self.request.query_params.get(conf.SHOP_CART)
        if is_in_shopping in conf.SYMBOL_TRUE_SEARCH:
            queryset = queryset.filter(cart=user.id)
        elif is_in_shopping in conf.SYMBOL_FALSE_SEARCH:
            queryset = queryset.exclude(cart=user.id)

        is_favorited = self.request.query_params.get(conf.FAVORITE)
        if is_favorited in conf.SYMBOL_TRUE_SEARCH:
            queryset = queryset.filter(favorite=user.id)
        if is_favorited in conf.SYMBOL_FALSE_SEARCH:
            queryset = queryset.exclude(favorite=user.id)

        return queryset

    @action(methods=conf.ACTION_METHODS, detail=True)
    def favorite(self, request, pk):
        return self.add_del_obj(pk, conf.FAVORITE_M2M)

    @action(methods=conf.ACTION_METHODS, detail=True)
    def shopping_cart(self, request, pk):
        return self.add_del_obj(pk, conf.SHOP_CART_M2M)

    @action(methods=('get',), detail=False)
    def download_shopping_cart(self, request):
        user = self.request.user
        if not user.carts.exists():
            return Response(status=HTTP_400_BAD_REQUEST)
        ingredients = AmountIngredient.objects.filter(
            recipe__in=(user.carts.values('id'))
        ).values(
            ingredient=F('ingredients__name'),
            measure=F('ingredients__measurement_unit')
        ).annotate(total=Sum('total'))

        filename = f'{user.username}_shopping_list.txt'
        shopping_list = (
            f'Список покупок для:\n\n{user.first_name}\n\n'
            f'{timezone.now().strftime(conf.DATE_TIME_FORMAT)}\n\n'
        )
        for ing in ingredients:
            shopping_list += (
                f'{ing["ingredient"]}: {ing["amount"]} {ing["measure"]}\n'
            )

        shopping_list += '\n\nПосчитано в Foodgram'

        response = HttpResponse(
            shopping_list, content_type='text.txt; charset=utf-8'
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
