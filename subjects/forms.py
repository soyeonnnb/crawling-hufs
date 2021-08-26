from django import forms
from . import models


class SubjectSearchForm(forms.Form):

    year = forms.IntegerField(required=True)
    track = forms.ModelChoiceField(queryset=models.Track.objects.all(), required=True)
    subjects = forms.ModelMultipleChoiceField(
        queryset=models.Subject.objects.all(), widget=forms.CheckboxSelectMultiple
    )
