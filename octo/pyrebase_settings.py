import pyrebase

config = {
    "apiKey": "<censored>",
    "authDomain": "<censored>",
    "databaseURL": "<censored>",
    "storageBucket": "<censored>",
    "serviceAccount": "<censored>"
}

firebase = pyrebase.initialize_app(config)
