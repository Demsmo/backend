from pyexpat import model
from .models import Order
from rest_framework import serializers

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = '__all__'