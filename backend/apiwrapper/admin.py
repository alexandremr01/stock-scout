from django.contrib import admin
from .models import StockTimeSeries, CoinQuotation

# Register your models here.
admin.site.register(StockTimeSeries)
admin.site.register(CoinQuotation)
