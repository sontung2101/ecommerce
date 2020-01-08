from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def quantri(request):
    return render(request, 'admin/admin.html')
