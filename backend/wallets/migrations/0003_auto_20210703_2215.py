# Generated by Django 3.2.2 on 2021-07-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_operations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
