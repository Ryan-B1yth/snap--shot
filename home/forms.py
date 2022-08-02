""" Imports """
from django import forms
from .models import Testimony


class TestimonyForm(forms.ModelForm):
    """ Testimony form """

    class Meta:
        """ Meta data """
        model = Testimony
        fields = '__all__'

        widgets = {
            'user': forms.HiddenInput(),
            'body': forms.Textarea(attrs={
                'placeholder': 'What would you like to say?',
            }
            )
        }
