from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientRegistrationForm
import pyrebase

config = {
    "apiKey": "AIzaSyDq1PSViG6o4yhxaqZ6ftezbNxIATqy5FU",
    "authDomain": "covid-monitoring-system.firebaseapp.com",
    "databaseURL": "https://covid-monitoring-system.firebaseio.com",
    "storageBucket": "covid-monitoring-system.appspot.com",
    "serviceAccount": "covidmonitor.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()


def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            phoneNo = form.cleaned_data.get('phoneNo')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            temperature = form.cleaned_data.get('temperature')
            bp = form.cleaned_data.get('bp')
            spo2 = form.cleaned_data.get('spo2')
            rr = form.cleaned_data.get('rr')
            password = form.cleaned_data.get('password1')

            data = {'firstname': firstname, 'lastname': lastname, 'phoneNo': phoneNo, 'email': email,
                    'gender': gender, 'temperature': temperature, 'bp': bp, 'spo2': spo2, 'rr': rr}

            auth.create_user_with_email_and_password(email, password)
            db.child('Patients').child(email).set(data)

            return redirect('newPatient')
        else:
            message2 = "Please recheck and fill the form again"
            form = PatientRegistrationForm()
            return render(request, 'patients/patientRegister.html', {'form': form, 'message':message2 })
    else:
        form = PatientRegistrationForm()
        message2 = ""
        return render(request, 'patients/patientRegister.html', {'form': form, 'message':message2})
