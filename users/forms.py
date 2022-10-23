from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Users


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    first_name =  forms.CharField(max_length=255, required=True)
    last_name =  forms.CharField(max_length=255, required=True)

    class Meta:
        model =  Users
        fields = (
            'first_name', 
            'last_name',
            'email',
        )

    def save(self, commit=True):
            user = super(CreateUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.is_active = False
            if commit:
                user.save()
            return user