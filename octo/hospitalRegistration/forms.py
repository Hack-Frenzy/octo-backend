from django import forms
from django.forms import CharField, Textarea, IntegerField, ChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HospitalBookForm(UserCreationForm):
    name = CharField(label="Hospital Name",
                     required=True,
                     strip=True)
    CHOICESTYPE=[('1','Government'),
         ('2','Private')]
    CHOICESHOSTYPE=[('1','Hospital'),
         ('2','Medical College / Institute'),
         ('3','Community Health Centre'),
         ('4','Corona Center'),
         ('5','Primary Health Centre'),
         ('6','Others'),]

    govOrPri = forms.ChoiceField(choices=CHOICESTYPE, widget=forms.RadioSelect,label="Are You")
    typeOfHos = forms.ChoiceField(choices=CHOICESHOSTYPE, widget=forms.RadioSelect,label="Health Care Provider Type")
    regNo = forms.IntegerField(label="Registration Number",required=True,)
    hospiAddress = CharField(label="Full Address ",
                required=True,
                strip=True)
    pincode = forms.IntegerField(label="Pincode",required=True,)
    class Meta:
            model= User
            fields = ['username','name','email','password1','password2','govOrPri','typeOfHos','regNo','hospiAddress','pincode']
    