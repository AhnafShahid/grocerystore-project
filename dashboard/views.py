from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')
    #return HttpResponse('<h1 style="color: DodgerBlue;"> This is the Index Page </h1>')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')
    #return HttpResponse('Staff page')

@login_required
def product(request):
    return render(request, 'dashboard/product.html')

@login_required
def order(request):
    return render(request, 'dashboard/order.html')
