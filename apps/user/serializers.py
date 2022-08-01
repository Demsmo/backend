import datetime
from pyexpat import model
from .models import User
from secrets import token_hex
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'email', 'password', 'token', 'token_expires_at')

class Usersignupserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only = True)
    token_expires_at = serializers.DateTimeField(read_only = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token', 'token_expires_at')


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['token'] = token_hex(30)
        validated_data['token_expires_at'] = datetime.datetime.now() + datetime.timedelta(days = 15)
        return super().create(validated_data) 


class Usersigninserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only = True)
    token_expires_at = serializers.DateTimeField(read_only = True)
    username = serializers.CharField(read_only = True)
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token', 'token_expires_at')

    def create(self, validated_data):
        user = User.objects.filter(email= validated_data['email'])
        if len(user) > 0 and check_password(validated_data['password'], user[0].password):
            user[0].token= token_hex(30)
            user[0].token_expires_at = datetime.datetime.now() + datetime.timedelta(days = 15)
            user[0].save()
            return user[0]
        else:
            raise serializers.ValidationError({'error': 'Password or Email is incorrect'})