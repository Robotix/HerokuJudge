"""
Django settings for testproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z6ex3!ov!vq4c$l$tn%k9x^&_va2(w$a+pe-(60+bg93y0$^u$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    BASE_DIR+'/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'solutions',
    'testResults',
    'social_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
'social.pipeline.social_auth.social_details',
'social.pipeline.social_auth.social_uid',
'social.pipeline.social_auth.auth_allowed',
'social_auth.backends.pipeline.social.social_auth_user',
'social_auth.backends.pipeline.associate.associate_by_email',
'social_auth.backends.pipeline.misc.save_status_to_session',
'social_auth.backends.pipeline.user.create_user',
'social_auth.backends.pipeline.social.associate_user',
'social_auth.backends.pipeline.social.load_extra_data',
'social_auth.backends.pipeline.user.update_user_details',
'social_auth.backends.pipeline.misc.save_status_to_session',
)

LOGIN_URL          = '/landingPage/'
LOGIN_REDIRECT_URL = '/landingPage/'
LOGIN_ERROR_URL    = '/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

FACEBOOK_APP_ID 					= '596534703784377'
FACEBOOK_API_SECRET					= '80584bb5bf55d84bd8d61f9b2e7ffd62'

GOOGLE_OAUTH2_CLIENT_ID				= '948756394788-hq2uule75a585h7ivk7raei301dppiah.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET			= '-xfOIxciKMxPiH-KSjZYlg6o '

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
# SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# SOCIAL_AUTH_UID_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
# SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd166ju7hou5g4v',
        'USER': 'suhnybmuyldehf',
        'PASSWORD': 'yMyW9pFlnq6eV2v0xoqqT8HLUM',
        'HOST': 'ec2-54-243-51-102.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

# Internationalization
# https://docs.djan,goproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


