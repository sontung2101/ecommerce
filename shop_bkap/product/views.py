from django.shortcuts import render
from product.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def product(request):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    products = Products.objects.all()
    count = Products.objects.count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    slide = {"mn": menu_list, "products": contacts, "count": count}
    return render(request, 'products/product.html', slide)


def productPro(request, question_id):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    products = Products.objects.filter(TypeProducts_id=question_id)
    count = Products.objects.filter(TypeProducts_id=question_id).count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    slide = {"mn": menu_list, "products": contacts, "count": count}
    return render(request, 'products/product.html', slide)


def productSale(request):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    products = Products.objects.filter(promotion_price__gt=0)
    count = Products.objects.count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    slide = {"mn": menu_list, "products": contacts, "count": count}
    return render(request, 'products/product.html', slide)


def productDetail(request,product_id):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    products = Products.objects.get(pk=product_id)
    related_products = Products.objects.filter(TypeProducts_id=products.TypeProducts_id)[:10]
    slide = {"mn": menu_list, "products": products,"products2":related_products}
    return render(request, 'productDetail/productDetail.html', slide)

