from django import forms
from .models import Pages

class PageForm(forms.ModelForm):
  class Meta:
    model = Pages
    fields = '__all__'
