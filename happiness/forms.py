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

    def __init__(self, *args, **kwargs):
        self.user = kwargs['initial']['user']
        super(HappinessForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        obj = super(HappinessForm, self).save(False)
        obj.user = self.user
        commit and obj.save()
        return obj

        