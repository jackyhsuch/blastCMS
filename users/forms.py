from django import forms

class NewUserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)