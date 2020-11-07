from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Todo

# def TodoAdmin(admin.ModelAdmin)
#     readonly_fields=('created',)

#admin.site.register(Todo, TodoAdmin)
admin.site.register(Todo)
