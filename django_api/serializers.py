from django_api.models import User
from rest_framework import serializers
from django_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
