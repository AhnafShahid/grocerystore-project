from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')
    #return HttpResponse('<h1 style="color: DodgerBlue;"> This is the Index Page </h1>')

def staff(request):
    return render(request, 'dashboard/staff.html')
    #return HttpResponse('Staff page')

def product(request):
    return render(request, 'dashboard/product.html')

def order(request):
    return render(request, 'dashboard/order.html')
