from django import forms
from django.forms import ModelMultipleChoiceField

from .models import Menu

class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_phone = forms.IntegerField()
    items = ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )