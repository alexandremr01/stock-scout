from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(unique=True)
    cpf_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
