import pyrebase
from decouple import config

config = {
    "apiKey": config('API_KEY'),
    "authDomain": config('AUTH_DOMAIN'),
    "databaseURL": config('DATABASE_URL'),
    "storageBucket": config('STORAGE_BUCKET'),
    "serviceAccount": config('SERVICE_ACCOUNT'),
}

firebase = pyrebase.initialize_app(config)
