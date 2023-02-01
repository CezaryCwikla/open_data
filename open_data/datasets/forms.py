from django import forms
from .models import Dataset


class DatasetCreationForm(forms.ModelForm):

    class Meta:
        model = Dataset
        fields = ['title',
                  'description',
                  'availability',
                  'tags',
                  'organisation',
                  'categories',
                  'resources']


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for k, v in self.Meta.labels.items():           #bez tego labels przy password nie będą działać
    #                                                     #wynika to z faktu, ze password1 i 2 są inaczej inicjalizowane
    #                                                     #niż reszta czyli username i email w klasie UserCreationForm
    #         self[k].label = v
