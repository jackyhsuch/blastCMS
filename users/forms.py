from django import forms

class NewUserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email Address', max_length=200)
    contact = forms.CharField(label='Contact Number',max_length=100)
    matric_number = forms.CharField(label= 'Matriculation Number',max_length=200)

 