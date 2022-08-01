from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(
        'Username', max_length= 50, blank= False, null= False, db_index= True
    )

    password = models.CharField(
        'Password', max_length= 500, blank= False, null= False, db_index= True
    )

    email = models.EmailField(
        'Email', max_length= 254, blank= False, null= False, db_index= True
    )

    token = models.CharField(
        'Token', max_length= 500
    )

    token_expires_at = models.DateTimeField(
        'Token Expires At'
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )