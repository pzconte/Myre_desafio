from django.contrib import admin

# Register your models here.

from .models import Project, School, Grade, Student, Project_data, Student_grade

admin.site.register(Project)
admin.site.register(School)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Project_data)
admin.site.register(Student_grade)