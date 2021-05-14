from django.http import JsonResponse
from django.shortcuts import render
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


def index(request):
    return render(request, template_name='index.html')

def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'Deploy automático da main atualizado!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
        ]
    })
    return response
