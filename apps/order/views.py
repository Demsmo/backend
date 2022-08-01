from django.shortcuts import render
from rest_framework import generics
from .serializers import Orderserializer
from .models import Order
from apps.user.mixins import CustomLoginRequiredMixin
from apps.cart.models import Cart
from .forms import OrderForm
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class Orderadd(CustomLoginRequiredMixin ,generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer
    def get(self, request, *args, **kwargs):
        self.queryset = Cart.objects.order_by('created_at').filter(user = request.login_user)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id
        order_form = OrderForm(request.data)
        if not order_form.is_valid():
            response = Response({'error': 'request data is incorrect'}, status = status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'applications/json'
            response.renderer_context = {}
            return response
        order = order_form.save()

        serializer= Orderserializer([order], many=True)
        return Response(serializer.data[0])