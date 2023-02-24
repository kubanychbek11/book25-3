from django import forms
from . import models

class ShowBookForm(forms.ModelForm):
    class Meta:
        model = models.ShowBook
        fields = '__all__'