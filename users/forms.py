from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','phone',
        'user_type']
    # name = forms.CharField(max_length=200)

class SellerForm(forms.Form):
    sell = forms.CharField(max_length=100)
