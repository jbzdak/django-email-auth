__author__ = 'jb'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

    email = forms.EmailField(required=True)