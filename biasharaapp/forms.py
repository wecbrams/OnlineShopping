from django import forms
from biasharaapp.models import Products


class ProductsForm(forms.ModelForm):  # It is form created from model
    class Meta:  # provides additional informatioon of form
        model = Products
        fields = ['name', 'price', 'description']
