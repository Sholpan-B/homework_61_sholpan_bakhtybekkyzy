from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator

from webapp.models import Task


def max_len_validator(string):
    if len(string) < 100:
        raise ValidationError('Описание не должно быть короче 100 символов!')
    return string


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    summary = forms.CharField(max_length=100, validators=(MinLengthValidator(limit_value=3, message='Заголовок должен '
                                                                                                    'быть длиннее 2 '
                                                                                                    'символов!'),
                                                          CustomLenValidator()))
    description = forms.CharField(validators=(max_len_validator,))

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if Task.objects.filter(summary=summary).exists():
            raise ValidationError('Такой заголовок уже есть!')
        return summary
