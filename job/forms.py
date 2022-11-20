from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import *

GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
]


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_active']


class StudentCreate(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    class Meta:
        model = StudentUser
        fields = '__all__'


class RecuriterCreate(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)

    class Meta:
        model = Recruiter
        fields = '__all__'

