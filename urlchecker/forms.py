from django import forms

class UrlForm(forms.Form):
    your_url = forms.URLField()