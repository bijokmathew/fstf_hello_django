from django import forms
from .models import Item


class Form_item(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
