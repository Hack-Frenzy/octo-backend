from django.shortcuts import render
from .forms import HospitalBookForm
# Create your views here.

def HospitalUser(request):
    if request.method == 'POST':
        form=HospitalBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = HospitalBookForm()
    return render(request,'hospitalRegistration/userreg.html',{'form':form})

