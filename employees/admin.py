
from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "name",
        "email",
        "phone",
        "department",
        "designation",
        "date_of_joining",
        "status",
    )
    search_fields = ("employee_id", "name", "email")
    list_filter = ("department", "status")
