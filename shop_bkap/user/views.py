from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from user.models import CustomerUser


# Create your views here.
def signup(request):
    error = ''

    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error = 'Confirmed password does not match'
        else:
            try:
                user = CustomerUser.objects.create_user(
                    username=username,
                    full_name=fullname,
                    phone_number=phonenumber,
                    email=email,
                    password=password1)

                user = authenticate(username=username,
                                    password=password1)
                login(request, user)
                return redirect('/')

            except Exception as e:
                error = str(e)

    return render(request, 'registration/signup.html', {'error': error})
