from django.urls import path
from . import views

app_name='pizzas'

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('more_pizzas/', views.more_pizzas, name='more_pizzas'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
]
