import pyrebase

config = {
    "apiKey": "AIzaSyDq1PSViG6o4yhxaqZ6ftezbNxIATqy5FU",
    "authDomain": "covid-monitoring-system.firebaseapp.com",
    "databaseURL": "https://covid-monitoring-system.firebaseio.com",
    "storageBucket": "covid-monitoring-system.appspot.com",
    "serviceAccount": "covidmonitor.json"
}

firebase = pyrebase.initialize_app(config)