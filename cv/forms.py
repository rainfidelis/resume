from django import forms
from django.forms import ModelForm
from .models import ContactModel

class ContactForm(ModelForm):

    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message Body'})
        }
        
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': ''
        }
