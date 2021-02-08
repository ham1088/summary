from django.contrib import admin
from .models import Employee, Department


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department']
    list_filter = ['department']



class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
