from django import forms

from happiness.models import Happiness


class HappinessForm(forms.ModelForm):

    class Meta:
        model = Happiness
        fields = [
            'date',
            'diary',
            'rating',
            'error',   
        ]

        labels = {
            'date': 'Date',
            'diary': 'Diary',
            'rating': 'Rating',
            'error': 'Error',
        }
        