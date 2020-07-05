from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientRegistrationForm
from pyrebase_settings import firebase

db = firebase.database()
auth = firebase.auth()
zero = 0

@login_required
def register_patient(request):
    if request.method == 'POST':
        hospitalName = request.user.username
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            phoneNo = form.cleaned_data.get('phoneNo')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            aadharno = form.cleaned_data.get('aadharno')
            bloodgrp = form.cleaned_data.get('bloodgrp')
            temperature = form.cleaned_data.get('temperature')
            bp = 0
            spo2 = 0
            heartrate = 0
            rr = 0
            avpu = 0
            mews = 0
            password = str(phoneNo)
           
            data = {'firstname': firstname, 'lastname': lastname, 'phoneNo': phoneNo,  'email': email, 'gender': gender, 'age': age, 'aadharno': aadharno, 'bloodgrp': bloodgrp,'temperature': temperature, 'bp': bp, 'spo2': spo2, 'rr': rr, 'avpu':avpu, 'heartrate':heartrate, 'mews': mews }
            try:
                auth.create_user_with_email_and_password(email, password)
                # the user will be identified by his phoneNo
                db.child('Patients').child(
                    hospitalName).child(phoneNo).set(data)
                return redirect('user/')
            except:
                message2 = "Patient Already Exist with same Phone Number"
                form = PatientRegistrationForm()
                return render(request, 'patients/patientRegister.html', {'form': form, 'message': message2})
        else:
            message2 = form.errors
            form = PatientRegistrationForm()
            return render(request, 'patients/patientRegister.html', {'form': form, 'message': message2})
    else:
        form = PatientRegistrationForm()
        message2 = ""
        return render(request, 'patients/patientRegister.html', {'form': form, 'message': message2})
