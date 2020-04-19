from django.db import models
from auth_.models import MyUser

class ListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class List(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    # due_date = models.DateTimeField(auto_now_add = False)
    status = models.CharField(max_length = 200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = ListManager()

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    def __str__(self):
        return '{}: {}, {}'.format(self.name, self.created_at,  self.status)

class ToDoManager(models.Manager):
    pass

class ToDo(models.Model):
    STATUSES=(
        (1,'new'),
        (2,'in progress'),
        (3,'done')
    )
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='todos')
    status = models.IntegerField(choices=STATUSES)
    image = models.ImageField(upload_to='todo', null=True, blank=True)
    objects = ToDoManager()

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural="Todos"