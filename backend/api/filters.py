from django_filters import rest_framework as filters

from recipes.models import Ingredient, Recipe


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug'
    )
    is_favorited = filters.BooleanFilter(
        method='get_is_favorited'
    )
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = (
            'is_favorited',
            'is_in_shopping_cart',
            'author',
            'tags'
        )

    def get_author(self, queryset, author):
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author=author)
        return queryset

    def get_is_favorited(self, queryset, name, value):
        users = self.request.user
        if users.is_anonymous:
            return queryset
        if value:
            return Recipe.objects.filter(
                favorites__user=self.request.user
            )
        return Recipe.objects.all()

    def get_is_in_shopping_cart(self, queryset, name, value):
        users = self.request.user
        if users.is_anonymous:
            return queryset
        if value:
            return Recipe.objects.filter(
                carts__user=self.request.user
            )
        return Recipe.objects.all()


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Ingredient
        fields = ('name',)
