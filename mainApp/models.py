from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 200, null=False, blank=False)
    password = models.CharField(max_length = 128, null=False, blank=False)
    
    