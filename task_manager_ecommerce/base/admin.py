from django.contrib import admin
from .models import Employee, Task, Department

admin.site.register(Department)
admin.site.register(Task)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role')
    search_fields = ('user__username', 'department__name', 'role')

