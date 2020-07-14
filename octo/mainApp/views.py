from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pyrebase_settings import firebase


db = firebase.database()


@login_required
def allPatients(request):
    global db
    hospitalName = request.user.username
    if db.child('Patients').child(hospitalName).shallow().get().val():
        users_query = db.child('Patients').child(hospitalName).order_by_child('mews').start_at(0).end_at(14).get()
        users = users_query.val() # Pyrebase object gave the data
        content = []

        for user in reversed(users):
            content.append(users[user])
        # take only the second part of each entry i.e value corresponding to the key
        return render(request, 'mainApp/allpatients.html', {'content': content, 'hospitalName': hospitalName})
         # query created and Pyrebase object returned
    else:
        return redirect('newPatient') 


@login_required
def patientDetail(request, phoneNo):
    global db
    hospitalName = request.user.username
    # query created and Pyrebase object returned
    users_query = db.child('Patients').child(hospitalName).get()
    users = users_query.val()  # Pyrebase object gave the data
    content = []
    # phoneNo converted to string since it is an integer
    specific_user = users[str(phoneNo)]
    return render(request, 'mainApp/patientDetail.html', {'user': specific_user, 'hospitalName': hospitalName})
