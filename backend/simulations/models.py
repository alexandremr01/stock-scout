from django.db import models
from users.models import Profile

# Create your models here.
class Simulation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    initial_value = models.DecimalField(decimal_places=2, max_digits=11)
    monthly_contribution = models.DecimalField(decimal_places=2, max_digits=11)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=5)
    final_amount = models.DecimalField(decimal_places=2, max_digits=11)
    time = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name