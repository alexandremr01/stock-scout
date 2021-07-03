from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response

from .serializers import SimulationSerializer
from .models import Simulation
from users.models import Profile
import json
class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all().order_by('name')
    serializer_class = SimulationSerializer

    def list(self, request):
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        queryset = Simulation.objects.filter(profile = profile)
        serializer = SimulationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = request.user
        profile = Profile.objects.filter(user = user).first()
        sim = Simulation(profile=profile, name=body['name'], initial_value=body['initial_value'],
            monthly_contribution = body['monthly_contribution'], interest_rate = body['interest_rate'],
            final_amount = body['final_amount'], time = body['time'])
        sim.save()
        return Response(SimulationSerializer(sim).data)
        # return Response(SimulationSerializer(sim, .data)
