from django.contrib import admin
from .models import Wallet, User, Asset

# Register your models here.
admin.site.register(Wallet)
admin.site.register(User)
admin.site.register(Asset)
