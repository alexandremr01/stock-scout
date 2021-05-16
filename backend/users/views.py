from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
