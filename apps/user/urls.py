from django.urls import path
from . import views

urlpatterns = [
    path('', views.Userlist.as_view(), name='User list'),
    path('signup/', views.Usersignup.as_view(), name='User Signup'),
    path('signin/', views.Usersignin.as_view(), name='User Signin'),
    path('checklogin/', views.UserCheckLogin.as_view(), name='User Check Login'),
]
