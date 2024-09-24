from django import forms
from .models import Category, Feature

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'category', 'hours']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Feature Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hours'}),
        }
