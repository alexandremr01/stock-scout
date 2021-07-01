from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.StockDetail.as_view()),
    path('coins/', views.CoinDetail.as_view())
]
