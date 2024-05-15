from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from davomat.forms import StudentCreateForm
from davomat.models import Group, Student


@login_required
def group_students(request, group_id=None):
    if group_id:
        group = get_object_or_404(Group, id=group_id)
        if request.user != group.owner:
            # Redirect or handle unauthorized access
            return redirect('login')  # You need to define this URL name
    else:
        group = None

    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.group = group  # Assign the group to the student before saving
            student.save()
            return redirect('students', group_id=group_id)  # Redirect to the same page after successful creation
    else:
        form = StudentCreateForm()

    if group:
        students = Student.objects.filter(group=group)
    else:
        students = Student.objects.all()
    return render(request, 'student/students.html', {'form': form, 'students': students, 'group': group})


def students_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if student.group.owner == request.user:
        student.delete()
        return redirect('students', group_id=student.group.id)
    else:
        return redirect('students', group_id=student.group.id)

