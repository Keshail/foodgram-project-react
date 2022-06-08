from api.conf import MAX_LEN_RECIPES_CHARFIELD, MAX_LEN_RECIPES_TEXTFIELD
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, CharField, CheckConstraint,
                              DateTimeField, ForeignKey, ImageField,
                              ManyToManyField, Model,
                              PositiveSmallIntegerField, Q, TextField,
                              UniqueConstraint)
from django.db.models.functions import Length

CharField.register_lookup(Length)

User = get_user_model()


class Tag(Model):
    name = CharField(
        verbose_name='Тэг',
        max_length=MAX_LEN_RECIPES_CHARFIELD,
        unique=True,
    )
    color = CharField(
        verbose_name='Цветовой HEX-код',
        max_length=6,
        blank=True,
        null=True,
        default='FF',
    )
    slug = CharField(
        verbose_name='Слаг тэга',
        max_length=MAX_LEN_RECIPES_CHARFIELD,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('name', )

    def __str__(self) -> str:
        return f'{self.name} (цвет: {self.color})'


class Ingredient(Model):
    name = CharField(
        verbose_name='Ингредиент',
        max_length=MAX_LEN_RECIPES_CHARFIELD,
    )
    measurement_unit = CharField(
        verbose_name='Единицы измерения',
        max_length=MAX_LEN_RECIPES_CHARFIELD,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name', )

    def __str__(self) -> str:
        return f'{self.name} {self.measurement_unit}'


class Recipe(Model):
    name = CharField(
        verbose_name='Название блюда',
        max_length=MAX_LEN_RECIPES_CHARFIELD,
    )
    author = ForeignKey(
        verbose_name='Автор рецепта',
        related_name='recipes',
        to=User,
        on_delete=CASCADE,
    )
    favorite = ManyToManyField(
        verbose_name='Понравившиеся рецепты',
        related_name='recipes',
        to=User,
    )
    tags = ManyToManyField(
        verbose_name='Тег',
        related_name='recipes',
        to='Tag',
    )
    ingredients = ManyToManyField(
        verbose_name='Ингредиенты блюда',
        related_name='recipes',
        to=Ingredient,
        through='recipes.AmountIngredient',
    )
    cart = ManyToManyField(
        verbose_name='Список покупок',
        related_name='recipes',
        to=User,
    )
    pub_date = DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    image = ImageField(
        verbose_name='Изображение блюда',
        upload_to='recipe_images/',
    )
    text = TextField(
        verbose_name='Описание блюда',
        max_length=MAX_LEN_RECIPES_TEXTFIELD,
    )
    cooking_time = PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        default=0,
        validators=(
            MinValueValidator(
                1,
                'Ваше блюдо уже готово!'
            ),
            MaxValueValidator(
                600,
                'Очень долго ждать...'
            ),
        ),
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )

    def __str__(self) -> str:
        return f'{self.name}. Автор: {self.author.username}'


class AmountIngredient(Model):
    recipe = ForeignKey(
        verbose_name='В каких рецептах',
        related_name='ingredients',
        to=Recipe,
        on_delete=CASCADE,
    )
    ingredients = ForeignKey(
        verbose_name='Связанные ингредиенты',
        related_name='ingredients',
        to=Ingredient,
        on_delete=CASCADE,
    )
    amount = PositiveSmallIntegerField(
        verbose_name='Количество',
        default=0,
        validators=(
            MinValueValidator(
                1, 'Нужно хоть какое-то количество.'
            ),
            MaxValueValidator(
                10000, 'Слишком много!'
            ),
        ),
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Количество Ингредиентов'
        ordering = ('recipe', )
        constraints = (
            UniqueConstraint(
                fields=('recipe', 'ingredients', ),
                name='\n%(app_label)s_%(class)s ingredient alredy added\n',
            ),
        )

    def __str__(self) -> str:
        return f'{self.amount} {self.ingredients}'
