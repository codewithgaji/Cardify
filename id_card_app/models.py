from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

# Create Choice Field
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]


# NIN Model
class NIN_IDCard(models.Model):                                                                                                                                                                                         
    full_name = models.CharField(max_length=250, default="Unknown")
    profile_pic = models.ImageField(upload_to='passports/', null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="Unknown")
    address = models.CharField(max_length=250, default="Unknown")
    nin = models.CharField(max_length=11)    
    dateofbirth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, default="Unknown")
    state_of_origin = models.CharField(max_length=250, default="Unknown")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

# Drivers License Model
class Drivers_license(models.Model):
     full_name = models.CharField(max_length=250, default="Unknown")
     dateofbirth = models.DateField(null=True, blank=True)
     placeofbirth = models.CharField(max_length=250)
     profile_pic = models.ImageField(upload_to='passports/', null=True)
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
     address = models.CharField(max_length=250, default="Unknown")
     phone_number = models.CharField(max_length=11)

     # License Info 
     license_number = models.CharField(max_length=50, default="Unknown")
     date_issued = models.DateField(null=True, blank=True)
     expiration_date = models.DateField(null=True, blank=True)
     license_type = models.CharField(max_length=10, default="Unknown")
     created_date = models.DateField(auto_now_add=True)

    
     def __str__(self):
        return self.full_name
     

# Business Model

class Business_Id(models.Model):                                                                                                                                                                            
    full_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='passports/', null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null = True)

    # Business info
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='passports/', null=True)
    phone_number = models.CharField(max_length=100)
    email_address = models.EmailField( default="Not provided yet")
    website = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return self.full_name
