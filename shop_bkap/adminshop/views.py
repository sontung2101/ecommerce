from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import decorators
from order.models import Partner
from product.models import *
from .form import *
from django.forms import modelformset_factory, inlineformset_factory


@decorators.login_required(login_url='/quantri/login_admin')
def listProduct(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        products = Products.objects.all()
        return render(request, 'products/list.html', {'products': products})


@decorators.login_required(login_url='/quantri/login_admin')
def createProduct(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        ImageFormset = modelformset_factory(Images, form=ImageForm, extra=3, max_num=3)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            formset = ImageFormset(request.POST or None, request.FILES or None)

            if form.is_valid() and formset.is_valid():
                post = form.save(commit=False)
                # post.author = request.user
                post.save()

                for f in formset:
                    try:
                        photo = Images(product=post, image=f.cleaned_data.get('image'))
                        photo.save()
                    except Exception as e:
                        break
                return redirect('adminshop:product-list')
        else:
            form = ProductForm()
            formset = ImageFormset(queryset=Images.objects.none())
        return render(request, 'products/form.html', {'form': form, 'formset': formset})


@decorators.login_required(login_url='/quantri/login_admin')
def updateProduct(request, id):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        post = get_object_or_404(Products, pk=id)
        ImageFormset = modelformset_factory(Images, form=ImageForm, extra=3, max_num=3)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=post)
            formset = ImageFormset(request.POST or None, request.FILES or None)
            if form.is_valid() and formset.is_valid():
                form.save()
                # print(formset.cleaned_data)
                data = Images.objects.filter(product=post)
                for index, f in enumerate(formset):
                    if f.cleaned_data:
                        # print(index)
                        if f.cleaned_data['id'] is None:
                            photo = Images(product=post, image=f.cleaned_data.get('image'))
                            photo.save()
                        # elif f.cleaned_data.get('image') is False :
                        #     photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        #     photo.delete()
                        #     # print(data[index].id)
                        #     # break
                        else:
                            photo = Images(product=post, image=f.cleaned_data.get('image'))
                            d = Images.objects.get(id=data[index].id)
                            d.image = photo.image
                            d.save()
                return redirect('adminshop:product-list')
        else:
            form = ProductForm(instance=post)
            formset = ImageFormset(queryset=Images.objects.filter(product=post))
        return render(request, 'products/form.html', {'form': form, 'formset': formset})


@decorators.login_required(login_url='/quantri/login_admin')
def deleteProduct(request, id):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        p = get_object_or_404(Products, pk=id)
        p.delete()
        return redirect('adminshop:product-list')


@decorators.login_required(login_url='/quantri/login_admin')
def tatCaDuyetDon(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        order = Partner.objects.filter(active=False, cancel=False)
        return render(request, 'duyet-don.html', {'order': order})


@decorators.login_required(login_url='/quantri/login_admin')
def tatCaDonDaDuyet(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        order = Partner.objects.filter(active=True)
        return render(request, 'da-duyet.html', {'order': order})


@decorators.login_required(login_url='/quantri/login_admin')
def tatCaDonDahuy(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        order = Partner.objects.filter(cancel=True)
        return render(request, 'da-huy.html', {'order': order})


# Create your views here.
@decorators.login_required(login_url='/quantri/login_admin')
def duyetDon(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    elif request.is_ajax():
        id = request.POST.get('id')
        err = ''
        try:
            active = True
            editPartner = Partner.objects.get(pk=id)
            editPartner.active = active
            editPartner.save()
        except Exception as e:
            err = str(e)
        return HttpResponse('OK')


@decorators.login_required(login_url='/quantri/login_admin')
def huyDuyet(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    elif request.is_ajax():
        id = request.POST.get('id')
        err = ''
        try:
            active = False
            editPartner = Partner.objects.get(pk=id)
            editPartner.active = active
            editPartner.save()
        except Exception as e:
            err = str(e)
        return redirect('adminshop:order-management')


@decorators.login_required(login_url='/quantri/login_admin')
def boHuyDon(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    elif request.is_ajax():
        id = request.POST.get('id')
        try:
            cancel = False
            editPartner = Partner.objects.get(pk=id)
            editPartner.cancel = cancel
            editPartner.save()
        except Exception as e:
            err = str(e)
        return redirect('adminshop:order-management')


@decorators.login_required(login_url='/quantri/login_admin')
def orderDetail(request, id):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        partner = Partner.objects.get(pk=id)
        content = {'parter': partner}
        return render(request, 'order-detail.html', content)


@decorators.login_required(
    login_url='/quantri/login_admin')  # kiểm tra tài khoản đã đăng nhập hay chưa nếu chưa dẫn link
def quanTri(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        return render(request, 'index.html')


@decorators.login_required(login_url='/quantri/login_admin')
def orderManagement(request):
    if request.user.is_staff != 1:
        return redirect('home:index')
    else:
        order = Partner.objects.all()
        return render(request, 'order-management.html', {'order': order})


class loginAdmin(View):
    def get(self, request):
        return render(request, 'login-admin.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None or my_user.is_staff == 0:  # nếu không có my_user trong user của django
            err = 'Đăng nhập thất bại'
            return render(request, 'login-admin.html', {'err': err})

        login(request, my_user)  # kiểm tra đăng nhập và chuyển trang
        return render(request, 'index.html')
