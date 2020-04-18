from django.db import models
from rest_framework import serializers


class BookJournalBase(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateField(null=True)

    def round_price(self):
        return round(self.price, 2)

    def short_name(self):
        raise NotImplementedError()

    class Meta:
        abstract = True

class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)

# def valid_num_pages(value):
#     if (value <= 0):
#         raise serializers.ValidationError('invalid num of pages')


class Journal(BookJournalBase):
    Bullet = 1
    Food = 2
    Travel = 3
    Sport = 4
    TYPE = (
        (Bullet, 'bullet'),
        (Food, 'food'),
        (Travel, 'travel'),
        (Sport, 'sport'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE, default=Sport)

    publisher = models.CharField(max_length=200)



