from django.urls import path
from adminshop import views

app_name = 'adminshop'
urlpatterns = [
    path('', views.quanTri, name='quantri'),
    path('login_admin/', views.loginAdmin.as_view(), name='login-admin'),
    path('order_management', views.orderManagement, name='order-management'),
    path('order_detail/<int:id>', views.orderDetail, name='order-detail'),
    path('duyet_don', views.duyetDon, name='duyet-don'),
    path('huy_duyet', views.huyDuyet, name='huy-duyet'),
    path('bo_huy_don', views.boHuyDon, name='bo-huy-don'),
    path('tat_ca_duyet_don',views.tatCaDuyetDon,name='tat-ca-duyet-don'),
    path('tat_ca_don_da_duyet', views.tatCaDonDaDuyet, name='tat-ca-don-da-duyet'),
    path('tat_ca_don_da_huy', views.tatCaDonDahuy, name='tat-ca-don-da-huy'),
]
