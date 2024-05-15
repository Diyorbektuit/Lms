from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CustomUser
from .forms import NewUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid username or password')

    return render(request=request, template_name='auth/login.html')


def register_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = NewUserForm()
    return render(request=request, template_name='auth/register.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
