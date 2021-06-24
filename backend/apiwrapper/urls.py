from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.StockDetail.as_view())
]
