from rest_framework.serializers import ValidationError
from string import hexdigits

from recipes.models import AmountIngredient


def recipe_amount_ingredients_set(recipe, ingredients):
    for ingredient in ingredients:
        AmountIngredient.objects.get_or_create(
            recipe=recipe,
            ingredients=ingredient['ingredient'],
            amount=ingredient['amount']
        )


def check_value_validate(value, klass=None):
    if not str(value).isdecimal():
        raise ValidationError(
            f'{value} должно содержать цифру'
        )
    if klass:
        return klass.objects.filter(id=value).exists()


def is_hex_color(value):
    if len(value) not in (3, 6):
        raise ValidationError(
            f'{value} не правильной длины ({len(value)}).'
        )
    if not set(value).issubset(hexdigits):
        raise ValidationError(
            f'{value} не шестнадцатиричное.'
        )


incorrect_layout = str.maketrans(
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'йцукенгшщзхъфывапролджэячсмитьбю.'
)
