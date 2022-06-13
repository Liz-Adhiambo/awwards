from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    '''
    This class will define the form for users to rate the project
    '''
    


    class Meta:
        model = Rating
        fields = ["design","usability","content"]
