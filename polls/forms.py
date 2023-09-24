from django import forms
from .models import todoModel

class TodoForm(forms.ModelForm):
    todo_name_uz=forms.CharField()
    todo_name_en=forms.CharField()
    todo_name_ru=forms.CharField()

    description_uz=forms.CharField()
    description_en=forms.CharField()
    description_ru=forms.CharField()

    class Meta:
        model=todoModel
        exclude=('todo_name','description')