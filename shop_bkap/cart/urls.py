from django.urls import path
from cart import views

app_name = 'cart'
urlpatterns = [
    path('addcart', views.addcart, name='addcart'),
    path('', views.shoppingcart.as_view(), name='shoppingcart'),
]
