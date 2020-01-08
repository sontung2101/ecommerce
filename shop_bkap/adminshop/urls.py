from django.urls import path
from adminshop import views

app_name = 'adminshop'
urlpatterns = [
    path('', views.quantri, name='quantri'),
]
