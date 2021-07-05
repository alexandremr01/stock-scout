from django.db import models
from users.models import Profile

# Create your models here.

class Wallet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Operations(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    type = models.CharField(max_length=5)
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    day = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Operations"
