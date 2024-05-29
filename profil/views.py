from django.shortcuts import render, redirect
from Auth.models import CustomUser
from .forms import NameUpdateForm, PasswordUpdateForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordUpdateForm


def profile(request):
    if request.user.is_authenticated:
        context = {
                  "username": request.user.username,
                  "first_name": request.user.first_name,
                  "last_name": request.user.last_name,
                  "email": request.user.email,
                  "date_joined": request.user.date_joined,
                  "last_login": request.user.last_login,
                  }
        return render(request, 'profile/profile.html', context)
    else:
        return redirect('login')


def update_name(request):
    user = CustomUser.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = NameUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = NameUpdateForm(instance=user)
    return render(request, 'profile/profile_update.html', {'form': form})



