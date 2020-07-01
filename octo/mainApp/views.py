from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pyrebase_settings import firebase


db = firebase.database()
# query created and Pyrebase object returned
users_query = db.child('Patients').get()
users = users_query.val()  # Pyrebase object gave the data
content = []
for user in users:
    # take only the second part of each entry i.e value corresponding to the key
    content.append(users[user])


@login_required
def allPatients(request):
    return render(request, 'mainApp/allpatients.html', {'content': content})
