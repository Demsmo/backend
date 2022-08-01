from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Orderadd.as_view(), name='order add'),
]
