from django import forms
from django.forms import CharField, Textarea, IntegerField, ChoiceField, CheckboxSelectMultiple, ImageField,FileField,MultipleChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HospitalBookForm(UserCreationForm):
     name = CharField(label="Hospital Name",
                    required=True,
                    strip=True)
     hospiAddress = CharField(label="Full Address ",
               required=True,
               strip=True)
     pincode = forms.IntegerField(label="Pincode",required=True,)
     phICU = forms.IntegerField(label="ICU Contact Number",required=True,)
     phSuperDoc = forms.IntegerField(label="Supervising Doctor's Contact No",required=True,)
     phHospi = forms.IntegerField(label="Hospital's contact No",required=True,)
     piAmb = forms.IntegerField(label="Ambulance Contact  No",required=True,)
     CATEGORYTYPE=[('1','L1'),
         ('2','L2'),
         ('3','L3'),
         ('4','Monitoring ')]
     category1 = forms.MultipleChoiceField(choices=CATEGORYTYPE, widget=forms.CheckboxSelectMultiple,label="Category of Covid Patients allowed")
     YesNoforApprove=[('1','Yes'),
     ('2','No'),] 
     YesorNO = forms.ChoiceField(choices=YesNoforApprove, widget=forms.RadioSelect,label="Approved to treat Covid-19 Patients")
     CHOICESTYPE=[('1','Government'),
         ('2','Private')]
     BedNo = forms.IntegerField(label="Total Number of Beds For Covid Patients",required=True,)

     CHOICESHOSTYPE=[('1','Hospital'),
         ('2','Medical College / Institute'),
         ('3','Community Health Centre'),
         ('4','Corona Center'),
         ('5','Primary Health Centre'),
         ('6','Others'),]
     CostandAvailiable=forms.ImageField(label="Cost and Avaliability")
     noOfPeopleMonitored=forms.IntegerField(label="No. of People To be Monitored",required=True,)
     HospitalDirectives=forms.ImageField(allow_empty_file=False,label="Hospital Directives")
     govOrPri = forms.ChoiceField(choices=CHOICESTYPE, widget=forms.RadioSelect,label="Are You")
     typeOfHos = forms.ChoiceField(choices=CHOICESHOSTYPE, widget=forms.RadioSelect,label="Health Care Provider Type")
     regNo = forms.IntegerField(label="Registration Number",required=True,)

     class Meta:
          model= User
          fields = ['username','name','email','password1','password2','govOrPri','typeOfHos','regNo','CostandAvailiable','HospitalDirectives','hospiAddress','pincode','phICU','phSuperDoc','phHospi','piAmb','category1','YesorNO','BedNo','noOfPeopleMonitored']
    