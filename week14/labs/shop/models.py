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
    product_count = models.IntegerField(null=True)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ProductManager(models.Manager):
    pass

class ProductBase(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField(default=0, null=False)
    objects = ProductManager()

    class Meta:
        abstract=True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # def some_method(self):
    #     return


class Product(ProductBase):
    STATUSES = (
        (1, 'in stock'),
        (2, 'sold out'),
    )
    image = models.ImageField(upload_to='products', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.IntegerField(choices=STATUSES)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'