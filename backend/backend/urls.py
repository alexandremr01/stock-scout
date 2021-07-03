"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from backend.views import index, simple_api_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_jwt.blacklist.views import BlacklistView
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('api/', include('wallets.urls')),
    path('api/', include('users.urls')),
    path('api/', include('apiwrapper.urls')),
    path('api/', include('simulations.urls')),

    re_path(r'^auth/obtain_token/', obtain_jwt_token),
    re_path(r'^auth/refresh_token/', refresh_jwt_token),
    path("auth/logout/", BlacklistView.as_view({"post": "create"})),

    path('admin/', admin.site.urls),
    re_path('^.*$', index),
]