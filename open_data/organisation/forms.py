from django import forms
from .models import Organisation


class OrganisationCreationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = ['title',
                  'phone',
                  'description',
                  'address',
                  'email',
                  'categories',
                  'users']
