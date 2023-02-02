from .models import Category
from django import forms


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title']