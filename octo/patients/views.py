from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientRegistrationForm
from pyrebase_settings import firebase

db = firebase.database()
auth = firebase.auth()


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
            temperature = form.cleaned_data.get('temperature')
            bp = form.cleaned_data.get('bp')
            spo2 = form.cleaned_data.get('spo2')
            rr = form.cleaned_data.get('rr')
            password = str(phoneNo)

            data = {'firstname': firstname, 'lastname': lastname, 'phoneNo': phoneNo, 'email': email,
                    'gender': gender, 'temperature': temperature, 'bp': bp, 'spo2': spo2, 'rr': rr}
            try:
                auth.create_user_with_email_and_password(email, password)
                # the user will be identified by his phoneNo
                db.child('Patients').child(
                    hospitalName).child(phoneNo).set(data)
                return redirect('newPatient')
            except:
                message2 = "User Already Exist with same PhoneNo"
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
