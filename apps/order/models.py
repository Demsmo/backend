# from tkinter import CASCADE
from django.db import models
from apps.user.models import User
# Create your models here.

class Order(models.Model):

    user_id = models.ForeignKey(
        User, blank= False, null= False, db_index= True, on_delete= models.CASCADE
    )

    total_price = models.FloatField(
        'Total Price', blank= False, null= False
    )

    full_name = models.CharField(
        'Full Name', max_length=25, blank= False, null= False
    )

    address_line1 = models.CharField(
        'Address Line 1', max_length= 250,blank= False, null= False
    )

    address_line2 = models.CharField(
        'Address Line 2', max_length= 250, blank= False, null= False
    )

    city = models.CharField(
        'City', max_length= 25, blank= False, null= False
    )

    state = models.CharField(
        'State', max_length= 25,blank= False, null= False
    )

    postal_code = models.IntegerField(
        'Postal Code', blank= False, null= False
    )

    country = models.CharField(
        'Country "United States"', max_length= 25, blank= False, null= False, default= 'United States'
    )

    telephone = models.IntegerField(
        'Telephone', blank= False, null= False
    )


    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )


