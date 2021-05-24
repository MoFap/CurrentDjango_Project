from django.contrib import admin
from .models import School, Faculty, Department, Certificate_type, Grade, Student


# Register your models here.

admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Certificate_type)
admin.site.register(Grade)
admin.site.register(Student)
