from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cartlist.as_view(), name='cart list'),
    path('add/', views.Cartadd.as_view(), name='cart add'),
    path('update/<int:pk>', views.Cartupdate.as_view(), name='cart update'),
    path('delete/<int:pk>', views.Cartdelete.as_view(), name='cart delete'),
]
