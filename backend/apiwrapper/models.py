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

    class Meta:
        verbose_name_plural = "Stocks time series"
