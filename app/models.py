from django.db import models

# Create your models here.

class Attendenc(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, null=True)
    entry_time = models.TimeField(auto_now_add=True, null=True)
    exit_time = models.TimeField(auto_now=True)

