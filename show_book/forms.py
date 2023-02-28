from django import forms
from . import models

class ShowBookForm(forms.ModelForm):
    class Meta:
        model = models.ShowBook
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.RatingBook
        fields = '__all__'