from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from product.models import *


# Create your views here.
def index(request):
    slide_list = Slide.objects.all()
    new_product = Products.objects.filter(new=1)[:10]
    slide = {"sl": slide_list,"products":new_product}
    return render(request, 'index/index.html', slide)


def base(request):
    return render(request, 'widgets/base.html')


def productDetail(request):
    return render(request, 'productDetail/productDetail.html')


def contact(request):
    return render(request, 'contact/contact.html')


def about(request):
    return render(request, 'about/about.html')


def blog(request):
    return render(request, 'blog/blog.html')


def blogDetail(request):
    return render(request, 'blogDetail/blogDetail.html')
