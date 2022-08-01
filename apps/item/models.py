from django.db import models
from cloudinary.models import CloudinaryField
import pytz

# Create your models here.

class Item(models.Model):

    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )

    STATUS_DICT = dict(STATUS)

    status = models.CharField(
        max_length=15, blank= False, null= False, db_index= True, default= 'inactive', choices=STATUS
    )

    name = models.CharField(
        'Name', max_length= 120, blank=False, null=False, db_index= True, 
    )

    price = models.IntegerField(
        blank=False, null=False, db_index= True,
    )

    image = CloudinaryField(
        'Image'
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )