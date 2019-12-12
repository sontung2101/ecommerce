from django.urls import path
from product import views
app_name = 'product'
urlpatterns = [
    path('productdetail<int:product_id>',views.productDetail,name='product-detail'),
    path('productsale',views.productSale,name='product-sale'),
    path('', views.product, name='product'),
    path('<int:question_id>', views.productPro, name='product-pro'),
]
