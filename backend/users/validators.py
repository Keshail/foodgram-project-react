from re import compile

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LineValidator:
    first_line = '[^а-яёА-ЯЁ]+'
    second_line = '[^a-zA-Z]+'
    message = (
        'Переданное значение на разных языках '
    )

    def __init__(self, first_line=None, second_line=None, message=None):
        if first_line is not None:
            self.first_line = first_line
        if second_line is not None:
            self.second_line = second_line
        if message is not None:
            self.message = message

        self.first_line = compile(self.first_line)
        self.second_line = compile(self.second_line)

    def __call__(self, value):
        if self.first_line.search(value) and self.second_line.search(value):
            raise ValidationError(self.message)


@deconstructible
class MinLenValidator:
    min_len = 0
    message = 'Значение слишком короткое.'

    def __init__(self, min_len=None, message=None):
        if min_len is not None:
            self.min_len = min_len
        if message is not None:
            self.message = message

    def __call__(self, value):
        if len(value) < self.min_len:
            raise ValidationError(self.message)
