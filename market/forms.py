from django import forms
from market.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'stock', 'image']
        # imagewidgets = {
        #     'image': forms.ClearableFileInput(attrs={'multiple': True})  # This allows multiple file uploads
        # }
