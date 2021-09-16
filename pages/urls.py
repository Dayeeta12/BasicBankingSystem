from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('newuser', views.newuser, name='newuser'),
    path('customer', views.customer, name='customer'),
    path('transfer/<str:pk>', views.transfer, name='transfer'),
    path('transactions', views.transactions, name='transactions'),
]
