from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

gender_choices = (('M', 'Male'),
                  ('F', 'Female'),
                  ('O', 'Others')
                  )

class User(AbstractUser):
   pass

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='M')
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=False, default='Address')
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    preferred_language = models.CharField(max_length=280, blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='craeted_id', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, blank=True, null=True, related_name='updated_id', on_delete=models.CASCADE)
    def __str__(self):
       return self.first_name+" "+self.last_name
