from pyexpat import model
from .models import Item
from rest_framework import serializers

class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = '__all__'