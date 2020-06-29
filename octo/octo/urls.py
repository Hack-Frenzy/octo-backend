from django.contrib import admin
from django.urls import path
from hospitalRegistration import views as hospitalRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',hospitalRegister.HospitalUser,name='HospitalUser'),
]
