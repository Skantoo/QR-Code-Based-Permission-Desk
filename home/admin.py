from django.contrib import admin
from home.models import Permissions, Student, Faculty

# Register your models here.
admin.site.register(Permissions) 
admin.site.register(Student) 
admin.site.register(Faculty)