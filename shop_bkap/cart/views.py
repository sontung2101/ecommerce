from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Products
# Create your views here.
from order.forms import oderForm
from cart.forms import cartForm
from django.template.loader import render_to_string
from django.views import View
import datetime
from cart.models import *
from user.models import CustomerUser

cart = {}


def addcart(request):
    if request.is_ajax():
        id = request.POST.get('id')
        num = request.POST.get('num')
        proDetail = Products.objects.get(pk=id)
        if proDetail.promotion_price == 0:
            if id in cart.keys():
                itemCart = {
                    'id': proDetail.id,
                    'name': proDetail.name,
                    'price': proDetail.unit_price,
                    'img': str(proDetail.image),
                    'num': int(cart[id]['num']) + int(num)
                }
            else:
                itemCart = {
                    'id': proDetail.id,
                    'name': proDetail.name,
                    'price': proDetail.unit_price,
                    'img': str(proDetail.image),
                    'num': num
                }
        else:
            if id in cart.keys():
                itemCart = {
                    'id': proDetail.id,
                    'name': proDetail.name,
                    'price': proDetail.promotion_price,
                    'img': str(proDetail.image),
                    'num': int(cart[id]['num']) + int(num)
                }
            else:
                itemCart = {
                    'id': proDetail.id,
                    'name': proDetail.name,
                    'price': proDetail.promotion_price,
                    'img': str(proDetail.image),
                    'num': num
                }

        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']
        html = render_to_string('cart/addcart.html', {'cart': cartInfo})

    return HttpResponse(html)


class shoppingcart(View):
    global cart
    global checkout
    checkout = False

    def get(self, request):
        total = 0
        carts = request.session.get('cart')
        if carts:
            for key, value in carts.items():
                total += int(value['price']) * int(value['num'])
            order = oderForm()
            # username = CustomerUser.objects.get(username=request.user.username)
            # name = username.full_name
            return render(request, 'cart/cart.html', {'total': total, 'order': order,})
        else:
            globals()['cart'] = {}
            return render(request, 'cart/cart.html')

    def post(self, request):
        phone_number = request.POST.get('phone_number')
        partner = Partner.objects.filter(phone_number=phone_number).first()
        order = oderForm(request.POST, instance=partner)
        if order.is_valid():
            partner = order.save()
            total = 0
            carts = request.session.get('cart')
            if carts:
                for key, value in carts.items():
                    total += int(value['price']) * int(value['num'])
                cart = Cart.objects.create(Partner=partner, total=total)
                for key, value in carts.items():
                    product = Products.objects.get(pk=value['id'])
                    cartitem = CartItem.objects.create(
                        Cart=cart,
                        Products=product,
                        quantity=value['num'],
                        unit_price=value['price']
                    )
                del request.session['cart']
                globals()['cart'] = {}
                checkout = True
                return render(request, 'cart/cart.html', {'checkout': checkout})
            else:
                return render(request, 'cart/cart.html')

        else:
            return HttpResponse('Validate')
