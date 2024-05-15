from davomat.models import Attendance, Mark, Group, Student
from django.shortcuts import render, redirect


def attendance(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.user == group.owner:
        students = Student.objects.filter(group=group)
        all_marks = []
        for student in students:
            marks = Mark.objects.filter(student=student)
            all_marks.append(marks)
        return render(request, 'attendance.html', {'marks': all_marks})
