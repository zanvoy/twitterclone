from django import forms

class RegesterForm(forms.Form):
    username = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)