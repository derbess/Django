from django.db import models
from auth_.models import MyUser
# Create your models here.

class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ProductManager(models.Manager):
    pass

class Product(models.Model):
    STATUSES = (
        (1, 'in stock'),
        (2, 'sold out'),
    )
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices=STATUSES)
    price = models.IntegerField(default=0, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'