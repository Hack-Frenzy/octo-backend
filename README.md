# octo-backend
The website of the COVCare project made using Django and Bootstrap.                              
Link to the website: https://praxiitr.eu-gb.cf.appdomain.cloud/

# COVCare: A COVID Quarantine and Isolation Home Healthcare Service

# Project Introduction

COVCare is a service to enable distant monitoring and constant evaluation of a large number of patients in the comfort of their homes and thus, home isolation and quarantine on a large scale can become a reality. This service comprises a website interface to be used by medical practitioners for continuous evaluation and a mobile application interface for the user to remain connected to the doctors.

# The Problem being addressed:
As the number of patients of COVID-19 continues to increase at an unpredictable rate, the number of beds in hospitals and centers set up by the government fall short of the requirement by a huge margin. The condition is so severe that the reports indicating the incidents of patients being kept on streets have surfaced recently. All patients are not required to be kept in specialized care units. Home quarantine and isolation with proper guidelines can be implemented in these less severe cases. This project is created to bridge the gap between the medical service provider and the patient.

# The Utility of the Project:
Specialized care is expensive and not required by everyone, this will provide an inexpensive alternative to conventional methods.
The extreme pressure on hospital beds will be reduced and more beds will be available to those in actual need.
Early and efficient intervention and identification of suspected patients will help reduce the spreading of this highly contagious infection.
Target users and prerequisites essential:

# Target users -
Corona Positive patients of the L1 category who do not require any specialized care. (ISOLATION)
Suspected patients who have come into contact with someone who was later detected positive for COVID-19. (QUARANTINE)
Post-treatment asymptomatic persons. (QUARANTINE)
Hospitals, government institutions, medical associations, and NGOs capable of monitoring patients. (MONITORING)
Prerequisites -
Thermometer, Sphygmomanometer, Smartphone, pulse-oximeter.
Relative or nurse to take down the parameters
PPE kit or other necessary apparatus / sanitization equipment.
Ability to follow home quarantine/isolation guidelines
Medical Background:
COVID-19: Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes. At this time (time of submission), there are no specific vaccines or treatments for COVID-19.
There are three categories of patients: L1, L2, and L3 with increasing order of severity.
The service makes use of the Modified Early Warning Score (MEWS) in order to evaluate the condition of the patient. It is a guide used by medical services to quickly determine the degree of illness of a patient. It is based on the vital signs. It is a scale from 0 to 14 based on 5 parameters. The parameters, as well as their corresponding values and MEWS score, is given:
top.png
caption (optional)
bp.png
caption (optional)
heartbeat.png
caption (optional)
rr.png
caption (optional)
avpu.png
caption (optional)
temperature.png
caption (optional)
Along with these parameters, this service has the provision of displaying SpO2 of a patient as well for additional information. SpO2, also known as oxygen saturation, is a measure of the amount of oxygen-carrying haemoglobin in the blood relative to the amount of haemoglobin not carrying oxygen. The normal value is between 94 to 100 %.
The patient will need to feed in these values on a regular basis.
A MEWS value below than 2 can be kept in home isolation.
A score ≥5 is statistically linked to increased likelihood of death or admission to an intensive care unit.
For any single physiological parameter scored +3, consider a higher level of care for patients.

# Details and working of the project:
This service has two interfaces, which we will individually deal with in the subsequent sections:
Patient service side
The patients can install the android app and create an account. There is a choice between three categories which were already mentioned in the target user section. The patient then creates an account with the hospital of their choice. If the hospital is available then the patient can log in the app using their phone number as password, which can be changed later. The patient (or an active relative or nurse) can update the medical parameters viz, BP, Temperature, SPO2, Respiratory Rate, and AVPU value. The values entered are timely updated in the database and are monitored by the hospital on the website.
Moreover, each parameter has a set of information about it for instance, What is blood pressure?, How do we measure it? and other guidelines to use the instrument along with links to online tutorials to do so.
Hospital service side:
Hospitals can register on the website by filling the sign-up form and can approve the registration of patients.
The dashboard of every hospital displays a list of patients by sorting them on the basis of their MEWS, displaying the more severe patients above and then the less severe once. The doctors can click on the specific patient account to see more details regarding his medical condition. Seeing the MEWS score and SPO2 values the doctors can decide which patients to immediately shift to the hospital.           
Here's a short video of the project made by us: https://youtu.be/Cymb4fwcoio
# Tech stack used:
Java: the android app has been written in the Java language with the help of Android Studio.          
Django: the website is written using the Django as the backend framework.               
Bootstrap: the frontend of the website is written using bootstrap.           
Firebase Authentication: To Authenticate Patients into the app.             
Firebase Realtime Database:  It has been used as the cloud backend service for the app.                 
PostgreSQL: the database management system of the website.                  
Heroku: It has been used to deploy the website of COVCare.                    
