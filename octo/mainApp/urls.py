from django.urls import path
from . import views

urlpatterns = [
    path('', views.allPatients, name='allPatients'),
    path('<int:phoneNo>/', views.patientDetail, name='patient-detail'),
    path('requests/', views.requests_patients, name='requests'),
    path('requests/contact/<str:uid>/', views.contactpatientDetail, name='contact-patient-detail'),
    path('requests/positive/<str:uid>/', views.covidpatientDetail, name='covid-patient-detail'),
    path('requests/postcovid/<str:uid>/', views.postcovidpatientDetail, name='postcovid-patient-detail')
]
