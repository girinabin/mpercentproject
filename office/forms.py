from django import forms
from .models import post

class Postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['firstname','lastname','department','operations']
