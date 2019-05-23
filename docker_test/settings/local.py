import os


# SECURITY WARNING: don't run with debug turned on in production!

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

SECRET_KEY = 'r-qhn2mnsitunp=l(#j1=0d)keow8e+af)x+4(@!d4xou(r5b7'

ALLOWED_HOSTS = ['0.0.0.0', '*']

WSGI_APPLICATION = 'docker_test.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

