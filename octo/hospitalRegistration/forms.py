from django import forms
from django.forms import CharField, Textarea, IntegerField, ChoiceField, CheckboxSelectMultiple, ImageField, FileField, MultipleChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HospitalBookForm(UserCreationForm):
    name = CharField(label="Hospital Name",
                     required=True,
                     strip=True)
    hospiAddress = CharField(label="Full Address ",
                             required=True,
                             strip=True)
    pincode = forms.IntegerField(label="Pincode", required=True,)
    phICU = forms.IntegerField(label="ICU Contact Number", required=True,)
    phSuperDoc = forms.IntegerField(
        label="Supervising Doctor's Contact No", required=True,)
    phHospi = forms.IntegerField(label="Hospital's contact No", required=True,)
    piAmb = forms.IntegerField(label="Ambulance Contact  No", required=True,)
    CATEGORYTYPE = [('L1', 'L1'),
                    ('L2', 'L2'),
                    ('L3', 'L3'),
                    ('Monitoring', 'Monitoring')]
    category1 = forms.MultipleChoiceField(
        choices=CATEGORYTYPE, widget=forms.CheckboxSelectMultiple, label="Category of Covid Patients allowed")
    YesNoforApprove = [('Yes', 'Yes'),
                       ('No', 'No'), ]
    YesorNO = forms.ChoiceField(
        choices=YesNoforApprove, widget=forms.RadioSelect, label="Approved to treat Covid-19 Patients")
    CHOICESTYPE = [('Government', 'Government'),
                   ('Private', 'Private')]
    BedNo = forms.IntegerField(
        label="Total Number of Beds For Covid Patients", required=True,)

    CHOICESHOSTYPE = [('Hospital', 'Hospital'),
                      ('Medical College / Institute', 'Medical College / Institute'),
                      ('Community Health Centre', 'Community Health Centre'),
                      ('Corona Center', 'Corona Center'),
                      ('Primary Health Centre', 'Primary Health Centre'),
                      ('Others', 'Others'), ]
    CostandAvailiable = forms.ImageField(label="Cost and Avaliability")
    noOfPeopleMonitored = forms.IntegerField(
        label="No. of People To be Monitored", required=True,)
    HospitalDirectives = forms.ImageField(
        allow_empty_file=False, label="Hospital Directives")
    govOrPri = forms.ChoiceField(
        choices=CHOICESTYPE, widget=forms.RadioSelect, label="Are You")
    typeOfHos = forms.ChoiceField(
        choices=CHOICESHOSTYPE, widget=forms.RadioSelect, label="Health Care Provider Type")
    regNo = forms.IntegerField(label="Registration Number", required=True,)

    def __init__(self, *args, **kwargs):
        super(HospitalBookForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2', 'govOrPri', 'typeOfHos', 'regNo', 'CostandAvailiable', 'HospitalDirectives',
                  'hospiAddress', 'pincode', 'phICU', 'phSuperDoc', 'phHospi', 'piAmb', 'category1', 'YesorNO', 'BedNo', 'noOfPeopleMonitored']
