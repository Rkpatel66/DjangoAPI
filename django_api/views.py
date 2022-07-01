from django.shortcuts import render
from django_api.models import User
from django_api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework .authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Userviewset(viewsets.ModelViewSet):
     serializer_class = UserSerializer
     queryset = User.objects.all()
     # authentication_classes=[BasicAuthentication]
     # permission_classes=[IsAuthenticated]
    