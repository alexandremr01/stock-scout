# serializers.py
from rest_framework import serializers
from .models import Simulation
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('email',)

class SimulationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Simulation
        fields = ('id', 'name', 'profile', 'created_at', 'initial_value', 'monthly_contribution', 'interest_rate', 'final_amount', 'time')

