from .models import Section, Song, Language, Line, Category
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model =  Category
        fields = ['name', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
