from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    
    def __str__(self):
        return self.user.username