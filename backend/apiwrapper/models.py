from django.db import models

# Create your models here.
class StockTimeSeries(models.Model):
    ticker = models.CharField(max_length=10)
    data = models.TextField(null=True)
    frequency = models.CharField(
        max_length = 10,
        choices = [
            ('DAY', 'Daily'),
            ('WEEK', 'Weekly'),
            ('MONTH', 'Monthly')
        ]
    )
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Stocks time series"
        unique_together = ('ticker', 'frequency')

class CoinQuotation(models.Model):
    name = models.CharField(max_length=10, unique=True)

    buy = models.FloatField()
    sell = models.FloatField(null=True, blank=True)
    variation = models.FloatField()

    last_modified = models.DateTimeField(auto_now=True)
