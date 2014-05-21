from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import person_attributes
from django.core.cache import cache
import urllib2
import json

class UserProfile(models.Model):  
    user = models.OneToOneField(User) 
    age = person_attributes.AgeField()
    country = person_attributes.CountryField(verbose_name='Country')
    gender = person_attributes.GenderField()
    

    some_date_field = models.DateTimeField(null=True, blank=True)
    some_bool_field = models.BooleanField(default=False)

    def __str__(self):  
          return "%s - %s %s [age:%s gender:%s country: %s date: %s bool: %s]" % (self.user, self.user.first_name, self.user.last_name, self.age, self.gender, self.country, self.some_date_field, self.some_bool_field)

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


