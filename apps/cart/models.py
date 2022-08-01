from django.db import models
from apps.order.models import Order
from apps.item.models import Item
from apps.user.models import User

# Create your models here.

class Cart(models.Model):
    # order_id = models.ForeignKey(
    #     Order, blank= False, null= False, db_index= True, on_delete= models.CASCADE
    # )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, blank= False, null= False
    )
    item = models.ForeignKey(
        Item, blank= False, null= False, db_index= True, on_delete= models.CASCADE
    )

    quantity = models.IntegerField(
        'Quantity', blank= False, null= False
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
