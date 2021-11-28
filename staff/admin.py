from django.contrib import admin
from .models import (
    Department,
    Staff,
    Employee,
    Position
)

admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Employee)
admin.site.register(Position)
