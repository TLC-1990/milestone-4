from django.db import models
from django.contrib.auth.models import User



class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    default_full_name = models.CharField(max_length=50, blank=True)
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_country = models.CharField(max_length=40, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_town_or_city = models.CharField(max_length=40, blank=True)
    default_street_address1 = models.CharField(max_length=80, blank=True)
    default_street_address2 = models.CharField(max_length=80, blank=True)
    default_county = models.CharField(max_length=80, blank=True)
    
    
    def __str__(self):
        return self.user.username
