from django.contrib import admin
from todo.main.models import Todo, TodoList
# Register your models here.

admin.site.register(Todo)
admin.site.register(TodoList)
# admin.site.register(Place)