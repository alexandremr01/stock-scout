from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
