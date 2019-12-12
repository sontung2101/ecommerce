from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('login', views.loginClass.as_view(), name='login'),
]