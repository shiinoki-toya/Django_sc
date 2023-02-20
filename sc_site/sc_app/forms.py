from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Sample

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = {'title','text'}
        widgets = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
        }
        labels = {
            'title':'タイトル',
            'text':'テキスト',
        }