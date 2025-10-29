from django import forms 
from .models import HRMmodel

class HRMForm(forms.ModelForm):
    class Meta:
        model = HRMmodel
        fields = "__all__"