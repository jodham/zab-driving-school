from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=254, required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class StaffCreateView(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=254, required=True)
    mobile = forms.CharField(max_length=15, required=True)

    class Meta:
        model = Staff
        fields = ['staffId', 'username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(StaffCreateView, self).__init__(*args, **kwargs)
        for fieldname in ['staffId', 'username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
