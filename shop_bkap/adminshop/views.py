from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import decorators
from order.models import Partner


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
