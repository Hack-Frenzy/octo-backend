from django.urls import path
from . import views

urlpatterns = [
    path('', views.allPatients, name='allPatients'),
    path('<str:email>/', views.patientDetail, name='patient-detail')
]
