from django import forms
from .models import post

class OperationRequest(forms.ModelForm):

    class Meta:
        model = post
        fields = ['firstname','lastname','department','operations']