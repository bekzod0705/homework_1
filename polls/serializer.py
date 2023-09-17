from rest_framework import serializers
from .models import todoModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todoModel
        fields=('__all__')
    def create(self,validated_data):
        validated_data['user']=get_object_or_404(User,username=self.context['request'].user)
        return super(ToDoSerializer,self).create(validated_data)
