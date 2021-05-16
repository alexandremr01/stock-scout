from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = [
            'email',
            'password',
            'cpf_number',
            'first_name',
            'last_name',
            'phone_number'
        ]
    
    def create(self, request):
        user = User.objects.create_user(
            username=request['email'],
            email=request['email'],
            password=request['password']
        )
        user.save()
        profile = Profile.objects.create(
            email=request['email'],
            cpf_number=request['cpf_number'],
            first_name=request['first_name'],
            last_name=request['last_name'],
            phone_number=request['phone_number'],
            user=user
        )
        profile.save()
        return profile
