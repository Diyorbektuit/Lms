from django.shortcuts import render, redirect

from davomat.forms import GroupCreateForm
from davomat.models import Group


# Create your views here.


def group_list(request):
    if request.user.is_authenticated:
        print(request.user)
        groups = Group.objects.filter(owner=request.user).order_by('name')
        return render(request, 'group/group_list.html', {'groups': groups})
    else:
        return redirect('login')


def group_delete(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.user == group.owner:
        group.delete()
        return redirect('home')
    else:
        return redirect('home')


def group_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GroupCreateForm(request.POST, request_user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = GroupCreateForm(request_user=request.user)
        return render(request, 'group/group_create.html', {'form': form})
    else:
        return redirect('login')
