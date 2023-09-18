from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()