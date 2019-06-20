from django import forms
from .models import Restaurant_name


class RateForm(forms.Form):
    your_rate = forms.IntegerField(max_value=5, min_value=0)
    your_review = forms.CharField(max_length=500)

class RestForm(forms.Form):
    Rest_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=200)
    img = forms.ImageField()