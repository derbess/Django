from django.db import models

from todo.auth_.models import MyUser
# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'


class Todo(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

