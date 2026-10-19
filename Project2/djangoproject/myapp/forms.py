from django import forms
from .models import Pet

class Pet_shop_form(forms.ModelForm):
  class Meta():
    model=Pet
    fields="__all__"
