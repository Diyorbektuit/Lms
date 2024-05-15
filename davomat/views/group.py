from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from davomat.forms import GroupCreateForm, GroupEditForm
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


@login_required
def group_edit(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.user != group.owner:
        return redirect('login')  # Or handle unauthorized access appropriately

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('students', group_id=group.id)  # Redirect to the group's student list
    else:
        form = GroupEditForm(instance=group)

    # Add the CSS class to the form field
    form.fields['name'].widget.attrs.update({'class': 'form-control'})

    return render(request, 'group/group_edit.html', {'form': form, 'group': group})
