from django import forms
from .models import Problem,Funding

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['locality', 'problem_type', 'description', 'image', 'geo_location']


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = ['upi_id', 'amount']
