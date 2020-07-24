from django.shortcuts import render, redirect
from .forms import HospitalBookForm
from pyrebase_settings import firebase

# Create your views here.
db = firebase.database()


def HospitalUser(request):
    global db
    if request.method == 'POST':
        form = HospitalBookForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data.get('username')
            regno = form.cleaned_data.get('regNo')    
            email = form.cleaned_data.get('email')    
            address = form.cleaned_data.get('hospiAddress')                        
            accesst = {'name': firstname,'regno':regno,'email':email,'address':address}
            try:
                # the user will be identified by his phoneNo
                db.child('HospitalInfo').child(
                    regno).set(accesst)
            except:
                message2 = "Patient Already Exist with same Phone Number"
            form.save()
            return redirect('login')
            
    else:
        form = HospitalBookForm()
    return render(request, 'hospitalRegistration/userreg.html', {'form': form})
