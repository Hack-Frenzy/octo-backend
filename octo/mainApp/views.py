from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def allPatients(request):
    return render(request,'mainApp/allpatients.html')
