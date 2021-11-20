from authentication.models import CustomUser
from django.db import models


class Offer(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f'NAME: {self.name}, USER: {self.user}, DESCRIPTION: {self.description}'

