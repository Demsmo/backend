from django.urls import path
from . import views

urlpatterns = [
    path('', views.Itemlist.as_view(), name='item list'),
]
