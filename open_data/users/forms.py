from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Nazwa użytkownika',
                  'email': 'Email',
                  'password1': 'Hasło',
                  'password2': 'Powtórz Hasło'
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():           #bez tego labels przy password nie będą działać
                                                        #wynika to z faktu, ze password1 i 2 są inaczej inicjalizowane
                                                        #niż reszta czyli username i email w klasie UserCreationForm
            self[k].label = v


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Nazwa użytkownika',
                  'email': 'Email'
                  }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

