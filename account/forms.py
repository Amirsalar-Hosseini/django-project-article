from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone number or email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone number or email address'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone number or email address'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone number or email address'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            raise ValidationError('this username is taken by another user')
        return username

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password1 != password2:
            raise ValidationError('password not match')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('this email is taken by another user')
        return email