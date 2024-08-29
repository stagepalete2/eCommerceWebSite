from django import forms

class SignInForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True, help_text='Enter your email')
    password = forms.PasswordInput()