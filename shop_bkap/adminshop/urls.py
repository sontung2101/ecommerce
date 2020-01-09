from django.urls import path
from adminshop import views

app_name = 'adminshop'
urlpatterns = [
    path('', views.quanTri, name='quantri'),
    path('login_admin/', views.loginAdmin.as_view(), name='login-admin'),
    path('order_management',views.orderManagement,name='order-management'),
]
