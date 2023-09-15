from rest_framework import serializers
from .models import todoModel

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todoModel
        fields=('__all__')

