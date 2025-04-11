from corsheaders.defaults import default_methods, default_headers
from pymongo import MongoClient

# MongoDB connection settings
MONGO_CLIENT = MongoClient('mongodb://localhost:27017/')
MONGO_DB = MONGO_CLIENT['octofit_db']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',  # Placeholder since we are using pymongo directly
    }
}

INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOW_HEADERS = list(default_headers)

ALLOWED_HOSTS = ['*']
