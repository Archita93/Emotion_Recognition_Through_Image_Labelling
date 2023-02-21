from .models import *
from django import forms
from django.db import models
from django.forms import fields

class UserImage(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'