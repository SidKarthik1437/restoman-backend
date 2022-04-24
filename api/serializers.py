from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer
from .models import Resto


class restoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resto
        fields = '__all__'


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'name', 'email', 'phone', 'password')
