from django import forms
from .models import Apk

class ApkForm(forms.ModelForm):
    class Meta:
        model = Apk
        fields = ['name', 'file']
