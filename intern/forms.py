from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile,Tasks


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Upload your work!',
        help_text='max. 42 megabytes',
    )

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['skills','resume','image']

class EditTask(forms.Form):
    comments=forms.CharField()
    isComplete=forms.BooleanField(required=False)