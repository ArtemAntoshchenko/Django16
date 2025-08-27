from django import forms
from .models import Books, Company, Product

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title','author','published_year','cost','pages','genre']

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','com']