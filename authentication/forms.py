from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)

class RegesterForm(forms.Form):
    username = forms.CharField(max_length =42)
    display_name = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)