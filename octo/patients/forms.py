from django import forms
from django.forms import CharField, IntegerField, ChoiceField, FloatField, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PatientRegistrationForm(UserCreationForm):
    CHOICESGENDER = [('Female', 'Female'), ('Male', 'Male'), ('Prefer not to tell', 'Prefer not to tell'), ]
    
    firstname = CharField(label="First Name", required=True, strip=True)
    lastname = CharField(label="Last Name", required=True, strip=True)
    phoneNo = IntegerField(label="Phone Number", required=True)
    email = CharField(label="Email Id", required=True, strip=True)
    gender = ChoiceField(choices=CHOICESGENDER,
                         widget=forms.RadioSelect, label="Gender")
    age =  IntegerField(label="Age", required=True)    
    aadharno =  IntegerField(label="Aadhar Number", required=True)  
    bloodgrp = CharField(label="Blood Group",max_length=5, required=True, strip=True)              
    # temperature = FloatField(label="Temperature",widget=forms.HiddenInput(), initial=0,disabled=True)
    # bp = FloatField(label="Blood Pressure", required=True, widget=forms.HiddenInput(), initial=0,disabled=True)
    # spo2 = FloatField(label="SpO2", widget=forms.HiddenInput(), initial=0,disabled=True)
    # rr = FloatField(label="R/R",widget=forms.HiddenInput(), initial=0,disabled=True)
    # mews = FloatField(label="Mews",widget=forms.HiddenInput(), initial=0,disabled=True)
    # The following function overwrites the __init__ function and removes the help text within password fields in the login template
    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            del self.fields[fieldname]
