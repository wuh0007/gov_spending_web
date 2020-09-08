from django import forms

# create a fetch form
class fetch_form(forms.Form):
    button = forms.CharField(required=False)
