from typing import ClassVar
from django.db import models
from django.forms import ModelForm,fields, widgets
from .models import Company
#models for registering the user
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#models for uploading data
from django.db import models


#for registering and auth the user
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1', 'password2']
        


class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'
        exclude=('owner',)
        widgets={
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'company_bio': forms.TextInput(attrs={'class':'form-control'}),
            'company_adress': forms.TextInput(attrs={'class':'form-control'}),
            'company_email': forms.TextInput(attrs={'class':'form-control'}),
            'company_phone': forms.TextInput(attrs={'class':'form-control'}),
            'company_facebook': forms.TextInput(attrs={'class':'form-control'}),
            'company_instagram': forms.TextInput(attrs={'class':'form-control'}),
            'company_website': forms.TextInput(attrs={'class':'form-control'}),
            'company_about': forms.Textarea(attrs={'class':'form-control'}),
            "company_pic" : forms.ClearableFileInput(attrs={'multiple': False}),
        }
