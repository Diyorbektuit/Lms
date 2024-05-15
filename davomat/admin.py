from django.contrib import admin
from .models import Group, Student, Attendance, Mark
# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name',)
    search_fields = ('name',)
    list_filter = ('owner',)


admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('group', 'last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    list_filter = ('group',)


admin.site.register(Student, StudentAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('group', 'date')
    search_fields = ('group', )
    list_filter = ('group', 'date')


admin.site.register(Attendance, AttendanceAdmin)


class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'attendance', 'mark')
    search_fields = ('student', )
    list_filter = ('student', 'mark')
    

admin.site.register(Mark, MarkAdmin)
