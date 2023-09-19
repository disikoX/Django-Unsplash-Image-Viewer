from django import forms

class FormName(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    botcatcher = forms.CharField(required = False,
                                  widget=forms.HiddenInput)


def clean_botcatcher(self):
    botcatcher = self.cleaned_data['botcatcher']
    if len(botcatcher) > 0:
        raise forms.ValidationError("GOTCHA BOT ! ")
    return botcatcher  