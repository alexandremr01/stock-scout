from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, request):
        user = User.objects.create_user(request['username'], request['email'], request['password'])
        user.save()
        return user
