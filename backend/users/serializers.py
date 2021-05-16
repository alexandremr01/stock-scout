from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Profile.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['email', 'password']
    
    def create(self, request):
        user = User.objects.create_user(
            username=request['email'],
            email=request['email'],
            password=request['password']
        )
        user.save()
        profile = Profile.objects.create(email=request['email'], user=user)
        profile.save()
        return profile
