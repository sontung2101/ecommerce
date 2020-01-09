from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import decorators
from order.models import Partner

# Create your views here.

@decorators.login_required(
    login_url='/quantri/login_admin')  # kiểm tra tài khoản đã đăng nhập hay chưa nếu chưa dẫn link
def quanTri(request):
    return render(request, 'index.html')


@decorators.login_required(login_url='/quantri/login_admin')
def orderManagement(request):
    order = Partner.objects.all()

    return render(request, 'order-management.html',{'order':order})


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
