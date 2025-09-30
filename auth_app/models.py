from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    
