from django.contrib import admin
from django.urls import path, include
from hospitalRegistration import views as hospitalRegister
from django.contrib.auth import views as auth_views
from patients.views import register_patient
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',hospitalRegister.HospitalUser,name='HospitalUser'),
    path('login/',auth_views.LoginView.as_view(template_name='mainApp/hospitalLogin.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='mainApp/hospitalLogout.html'),name='logout'),
    path('user/',include('mainApp.urls')),
    path('new_patient', register_patient, name='newPatient'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
