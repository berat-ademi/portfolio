from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Projects

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=101)
    class Meta:
        model = User
        fields = ['username', 'email', 'address','password1', 'password2']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'