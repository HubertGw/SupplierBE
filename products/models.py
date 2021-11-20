from authentication.models import CustomUser
from django.db import models
from offers.models import Offer


class Category(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'NAME: {self.name}'


class Product(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.DecimalField(max_length=20, null=False, blank=False, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return f'NAME: {self.name}, DESCRIPTION: {self.description}, PRICE: {self.price}, OFFER: {self.offer}'
