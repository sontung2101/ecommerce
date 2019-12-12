from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View


# Create your views here.
class loginClass(View):
    def get(self, request):
        return render(request, 'user/user.html', )

    def post(self, request):
        user_name = request.POST.get('tk')
        pass_word = request.POST.get('mk')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:  # nếu không có my_user trong user của django
            return HttpResponse('user khong ton tai')
        login(request, my_user)  # kiểm tra đăng nhập và chuyển trang
        return HttpResponse('Dang nhap thanh cong')
