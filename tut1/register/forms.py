from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
    # we want to save the user data in the user database
    # gotta import User
       model = User
        # we type in this fields the order we want them to 
        # appear in the form 
       fields = ["username", "email", "password1", "password2"]
       # password1 and 2 are built in to django