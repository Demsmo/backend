from pyexpat import model
from .models import Cart
from rest_framework import serializers

class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields = '__all__'
        depth = 1

class Cartaddserializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields = '__all__'