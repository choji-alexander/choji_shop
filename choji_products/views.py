from django.http import HttpResponse
from django.shortcuts import render
from .models import Choji_products


def index(request):
    choji_products = Choji_products.objects.all()
    return render(request, 'index.html', {'choji_products': choji_products})


def new(request):
    return HttpResponse('Boss new products')
