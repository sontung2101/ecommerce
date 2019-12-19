from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from user.models import CustomerUser
from order.models import Partner
from user.form import *
from cart.models import *


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


class editProfile(View):
    def get(self, request):
        return render(request, 'user/edit_profile.html')

    def post(self, request):
        err = ''
        try:
            user = request.user
            user.full_name = request.POST.get('full_name')
            user.email = request.POST.get('email')
            user.phone_number = request.POST.get('phone_number')
            user.save()
        except Exception as e:
            err = str(e)
        return render(request, 'home.html', {'err': err})


class orderManagement(View):
    def get(self, request):
        user_id = request.user.id
        partner = Partner.objects.filter(customeruser_id=user_id)
        # ----------------------------------------------------------------
        # cart = Cart.objects.select_related('Partner').filter(Partner__in=partner)
        # cartItem = CartItem.objects.select_related('Cart').filter(Cart__in=cart)
        # productId = cartItem.values_list('Products')
        # productImg= Products.objects.filter(pk__in=productId)
        # cartitem = CartItem.objects.filter(Cart=cart)
        # pro = Products.objects.get(pk=cartitem)
        # print(partner)
        # print(cart)
        # print(cartItem)
        # print(productId)
        # print(productImg)
        content = {'parter': partner}
        return render(request, 'user/order_management.html', content)

    def post(self, request):
        err = ''
        try:
            cancel = request.POST.get('cancel')
            id = request.POST.get('id')
            editPartner = Partner.objects.get(pk=id)
            editPartner.cancel = cancel
            editPartner.save()
        except Exception as e:
            err = str(e)
        return redirect('user:order-management')
