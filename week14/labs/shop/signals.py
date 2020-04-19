from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Category, Product


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        if category.product_count is None:
            Category.objects.filter(id=category.id)\
                .update(product_count=Category.objects.get(id=category.id).products.count())
        else:
            Category.objects.filter(id=category.id).update(product_count=category.product_count + 1)

@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, using, **kwargs):
        category = instance.category
        if category.product_count is None:
            Category.objects.filter(id=category.id)\
                .update(product_count=Category.objects.get(id=category.id).products.count())
        else:
            Category.objects.filter(id=category.id).update(product_count=max(category.product_count - 1, 0))