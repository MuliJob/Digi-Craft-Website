from django import forms

class NewsLetterForm(forms.Form):
    email = forms.EmailField(label='Email')

class MessageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone number', max_length=10)
    message = forms.CharField(label='Additional Message', max_length=1000)