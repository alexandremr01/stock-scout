from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(unique=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
