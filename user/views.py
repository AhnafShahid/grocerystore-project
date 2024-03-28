from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
           # user = form.save()
            form.save()
            #group = Group.objects.get(name='Customers')
            #user.groups.add(group)
            return redirect('dashboard-index')
           # return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {

        'form':form,

    }
    return render(request, 'user/register.html', {'form' : form})