import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

print(os.environ['SECRET_KEY'])
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['mydomain.com', '*']

WSGI_APPLICATION = 'docker_test.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DB_NAME_DJANGO'],
#         'USER': os.environ['DB_USER_DJANGO'],
#         'PASSWORD': os.environ['DB_PASSWORD_DJANGO'],
#         'HOST': os.environ['CLOUD_SQL_INSTANCE_IP'],
#         'PORT': 5432,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Add env vars in Admin console

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
