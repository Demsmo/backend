from django.shortcuts import render
from rest_framework import generics
from .serializers import Userserializer, Usersignupserializer, Usersigninserializer
from .models import User
from .mixins import CustomLoginRequiredMixin
from rest_framework.response import Response

# Create your views here.
class Userlist(generics.ListAPIView):
    queryset = User.objects.all()[:20]
    serializer_class = Userserializer

class Usersignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Usersignupserializer

class Usersignin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Usersigninserializer

class UserCheckLogin(CustomLoginRequiredMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer = Userserializer([request.login_user], many = True)
        return Response(serializer.data[0])
