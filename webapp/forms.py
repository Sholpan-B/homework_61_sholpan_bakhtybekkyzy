from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи'
        }

        def clean_title(self):
            summary = self.cleaned_data.get('summary')
            if len(summary) < 2:
                raise ValidationError('Заголовок должен быть длиннее 2 символов')
            return summary

