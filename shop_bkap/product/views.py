from django.shortcuts import render, redirect, HttpResponse
from product.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def product(request):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    productList = Products.objects.all()
    categoryList = TypeProducts.objects.filter(Q(type_parent=2) |Q(type_parent=3)|Q(type_parent=4)|Q(type_parent=5))
    queryParams = request.GET

    productName = queryParams.get('product_name')
    categoryId = queryParams.get('category_id')
    priceRange = queryParams.get('price_range')

    minPrice, maxPrice = None, None
    priceTable = {
        '1': [None, 5],
        '2': [5,10],
        '3': [10, 20],
        '4': [20, None]
    }

    if priceRange:
        minPrice, maxPrice = priceTable.get(priceRange)
    if productName:
        productList = productList.filter(name__icontains=productName)

    if categoryId:
        productList = productList.filter(TypeProducts__id=int(categoryId))

    if minPrice:
        productList = productList.filter(unit_price__gte=minPrice * 1e5)  # lớn hơn hoặc bằng
    if maxPrice:
        productList = productList.filter(unit_price__lte=maxPrice * 1e5)  # nhỏ hơn hoặc bằng
    pageSize = 6
    page = int(request.GET.get('page',1))
    paginator = Paginator(productList,pageSize)
    cur_items = paginator.get_page(page)
    slide = {"mn": menu_list,
             "products": cur_items,
             'page': page,
             'num_pages': paginator.num_pages,
             "count": paginator.count,
             'categoryList': categoryList,
             'queryParams': queryParams}
    return render(request, 'products/product.html', slide)


def productPro(request, question_id):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    productList = Products.objects.filter(TypeProducts_id=question_id)
    categoryList = TypeProducts.objects.filter(
        Q(type_parent=2) | Q(type_parent=3) | Q(type_parent=4) | Q(type_parent=5))
    queryParams = request.GET
    if request.GET.get('product_name') or request.GET.get('category_id') or request.GET.get('price_range'):
        productList = Products.objects.all()
        productName = queryParams.get('product_name')
        categoryId = queryParams.get('category_id')
        priceRange = queryParams.get('price_range')

        minPrice, maxPrice = None, None
        priceTable = {
            '1': [None, 5],
            '2': [5, 10],
            '3': [10, 20],
            '4': [20, None]
        }

        if priceRange:
            minPrice, maxPrice = priceTable.get(priceRange)
        if productName:
            productList = productList.filter(name__icontains=productName)

        if categoryId:
            productList = productList.filter(TypeProducts__id=int(categoryId))

        if minPrice:
            productList = productList.filter(unit_price__gte=minPrice * 1e5)  # lớn hơn hoặc bằng
        if maxPrice:
            productList = productList.filter(unit_price__lte=maxPrice * 1e5)  # nhỏ hơn hoặc bằng
    pageSize = 6
    page = int(request.GET.get('page', 1))
    paginator = Paginator(productList, pageSize)
    cur_items = paginator.get_page(page)
    slide = {"mn": menu_list,
             "products": cur_items,
             'page': page,
             'num_pages': paginator.num_pages,
             "count": paginator.count,
             'categoryList': categoryList,
             'queryParams': queryParams}
    return render(request, 'products/product.html', slide)


def productSale(request):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    productList = Products.objects.filter(promotion_price__gt=0)
    categoryList = TypeProducts.objects.filter(
        Q(type_parent=2) | Q(type_parent=3) | Q(type_parent=4) | Q(type_parent=5))
    queryParams = request.GET
    if request.GET.get('product_name') or request.GET.get('category_id') or request.GET.get('price_range'):
        productList = Products.objects.all()
        productName = queryParams.get('product_name')
        categoryId = queryParams.get('category_id')
        priceRange = queryParams.get('price_range')

        minPrice, maxPrice = None, None
        priceTable = {
            '1': [None, 5],
            '2': [5, 10],
            '3': [10, 20],
            '4': [20, None]
        }

        if priceRange:
            minPrice, maxPrice = priceTable.get(priceRange)
        if productName:
            productList = productList.filter(name__icontains=productName)

        if categoryId:
            productList = productList.filter(TypeProducts__id=int(categoryId))

        if minPrice:
            productList = productList.filter(unit_price__gte=minPrice * 1e5)  # lớn hơn hoặc bằng
        if maxPrice:
            productList = productList.filter(unit_price__lte=maxPrice * 1e5)  # nhỏ hơn hoặc bằng
    pageSize = 6
    page = int(request.GET.get('page', 1))
    paginator = Paginator(productList, pageSize)
    cur_items = paginator.get_page(page)
    slide = {"mn": menu_list,
             "products": cur_items,
             'page': page,
             'num_pages': paginator.num_pages,
             "count": paginator.count,
             'categoryList': categoryList,
             'queryParams': queryParams}
    return render(request, 'products/product.html', slide)


def productDetail(request, product_id):
    menu_list = TypeProducts.objects.filter(type_parent=0)
    products = Products.objects.get(pk=product_id)
    related_products = Products.objects.filter(TypeProducts_id=products.TypeProducts_id)[:10]
    slide = {"mn": menu_list, "products": products, "products2": related_products}
    return render(request, 'productDetail/productDetail.html', slide)
