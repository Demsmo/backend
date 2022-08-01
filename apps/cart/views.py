from django.shortcuts import render
from rest_framework import generics
from .serializers import Cartaddserializer, Cartserializer
from .models import Cart
from apps.user.mixins import CustomLoginRequiredMixin
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class Cartlist(CustomLoginRequiredMixin,generics.ListAPIView):
    queryset = Cart.objects.order_by('created_at')
    serializer_class = Cartserializer
    def get(self, request, *args, **kwargs):
        self.queryset = Cart.objects.filter(user = request.login_user)
        return self.list(request, *args, **kwargs)
    def get_paginated_response(self, data):
       return Response(data)

class Cartadd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = Cartaddserializer
    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id
        return self.create(request, *args, **kwargs)

class Cartupdate(CustomLoginRequiredMixin,generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
    def update(self, request, *args, **kwargs):
        cart = Cart.objects.get(pk = self.kwargs['pk'])
        if cart.user.id != request.login_user.id:
            response = Response({'error': 'cannot update the cart not owned by you'}, status = status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'applications/JSON'
            response.renderer_context = {}
            return response
        cart.quantity = request.data['quantity']
        cart.save()
        serializer = Cartserializer([cart], many = True)
        return Response(serializer.data[0])

class Cartdelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class= Cartserializer
    def delete(self, request, *args, **kwargs):
        cart = Cart.objects.get(pk = self.kwargs['pk'])
        if cart.user.id != request.login_user.id:
            response = Response({'error': 'cannot delete items not added by you'}, status = status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'applications/JSON'
            response.renderer_context = {}
            return response
        return self.destroy(request, *args, **kwargs)