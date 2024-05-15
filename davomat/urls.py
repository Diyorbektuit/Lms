from django.urls import path
from .views import group, student, attendace
urlpatterns = [
    path('', group.group_list, name='home'),
    path('students/<int:group_id>/', student.group_students, name='students'),
    path('group_create/', group.group_create, name='group_create'),
    path('group_delete/<int:group_id>/', group.group_delete, name='group_delete'),
    path('student_delete/<int:student_id>/', student.students_delete, name='student_delete'),
    path('attendance/<int:group_id>/', attendace.attendance, name='attendance'),
]