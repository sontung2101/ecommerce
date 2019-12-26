from django.urls import path
from cart import views

app_name = 'cart'
urlpatterns = [
    path('updateCart', views.updateCart, name='updateCart'),
    path('addcart', views.addcart, name='addcart'),
    path('', views.shoppingcart.as_view(), name='shoppingcart'),
    path('deleteCart<int:product_cart_id>', views.deleteCart, name='deleteCart'),
]
