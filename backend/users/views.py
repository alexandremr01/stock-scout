from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse


class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)

class MeView(APIView):

    def get(self, request, format=None):
        profile = Profile.objects.filter(user=request.user).first()
        return JsonResponse({'name': profile.first_name})
