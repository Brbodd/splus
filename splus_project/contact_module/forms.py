from django import forms
from .models import ContactsUs

class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=200)
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(max_length=350)

class ContactsUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactsUs
        fields = ['title', 'full_name', 'email', 'message']
        widget = {
            'title' : {
                forms.TextInput
            },
            'full_name' : {
                forms.TextInput
            },
            'email': { 
                forms.EmailField 
            },
            'message': {
                forms.Textarea
            }
        }

        label = {
            'title' : {
                'عنوان'
            },
            'full_name' : {
                'نام و نام خانوادگی'
            },
            'email': { 
                'ایمیل' 
            },
            'message': {
                'متن پیام'
            }
        }

        error_messages = {
            'title' : {
                'required': 'لطفا عنوان را وارد کنید',
                'max_length': 'عنوان باید کمتر از ۲۰۰ کاراکتر باشد'
            },
            'full_name' : {
                'required': 'لطفا نام و نام خانوادگی را وارد کنید',
                'max_length': 'عنوان باید کمتر از ۲۰۰ کاراکتر باشد'                
            },
            'email': { 
                'required': 'لطفا عنوان را وارد کنید',
            },
            'message': {
                'required': 'لطفا متن پیام را وارد کنید',
                'max_length': 'عنوان باید کمتر از ۳۵۰ کاراکتر باشد'                
            }
        }

        required = {
            'title' : {
                True
            },
            'full_name' : {
                True
            },
            'email': { 
                True
            },
            'message': {
                True
            }
        }
