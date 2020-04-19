from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Min, Sum
from shop.models import Product, Category


class Command(BaseCommand):
    help = 'Get all categories'

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append(f'id: {category.id}, name: {category.name}, product_count: {category.product_count}')
        self.stdout.write(self.style.SUCCESS(data))