from django.db import models
from users.models import Profile

# Create your models here.

class Wallet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    created_at = models.DateField()
    def __str__(self):
        return self.name

class Asset(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    unit_value  = models.DecimalField(decimal_places=2, max_digits=11)
    created_at = models.DateField()
    def __str__(self):
        return self.name
