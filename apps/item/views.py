import imp
from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import generics
from .serializers import Itemserializer
from .models import Item

# Create your views here.
class Itemlist(generics.ListAPIView):
    queryset = Item.objects.order_by('created_at').filter(status = 'active')
    serializer_class = Itemserializer