from django.contrib.auth.models import User
from django.db import models


class Offer(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f'NAME: {self.name}, USER: {self.user}, DESCRIPTION: {self.description}'

class User(models.Model):
    name = models.TextField(max_length=12, null=False, blank=False)
    surname = models.TextField(max_length=100, null=False, blank=False)
    mail = models.TextField(max_length=100, null=False, blank=False)
    birthdate = models.TextField(max_length=100, null=False, blank=False)
    login = models.TextField(max_length=1000, null=False, blank=False)
    password = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f'NAME: {self.name}, USER: {self.user}, DESCRIPTION: {self.description}'


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login_view(user)
            return render(request, 'base_in/base_in.html', {})
        else:
            return render(request, 'signupapp/error.html', {'message': 'the acount is not active'})
    else:
        return render(request, 'signupapp/error.html', {'message': 'username and password is incorrect'})
