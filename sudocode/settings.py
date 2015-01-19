"""
Django settings for sudocode project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f(&c#7x3kkzea+t&kpv+@!jf=%wlih4mjro02tn7m3b(06zblj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Allow all host headers
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'django_pygments',
    'submission',
    'users',
    'testcases_theraidone',
    'submission_theraidone',
    'participant'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sudocode.urls'

WSGI_APPLICATION = 'sudocode.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da4abl57es557h',
        'USER': 'xeujnnexbxwkde',
        'PASSWORD': 'dEieJrTwnUA9zsNSdfRDoUmBnh',
        'HOST': 'ec2-54-204-40-140.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Static asset configuration

STATIC_URL = '/static/'
# STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

################################# Python Social Auth Settings #################################

## Backends
AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'social.backends.github.GithubOAuth2',
   'social.backends.disqus.DisqusOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

## Redirect URL options
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/user/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'

##  User Model
# SOCIAL_AUTH_USER_MODEL = 'django.contrib.auth.models.User'

## Username Generation
SOCIAL_AUTH_UUID_LENGTH = 16
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = False
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_CLEAN_USERNAMES = True

## Django Admin
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

## Disqus
SOCIAL_AUTH_DISQUS_KEY = '89Jtc2FY2hNbvIabTZ0UH6kdVOJ1Pf9OHZeel4DIiG4y8aD9vBNm3RNngRimBTo8'
SOCIAL_AUTH_DISQUS_SECRET = 'Bn5rDKBqrEvJ7N0kOKP4udotAz3Y4g1NXY5oNdUpFaKRWtJfekbKMPufTfkUcU4k'
SOCIAL_AUTH_DISQUS_AUTH_EXTRA_ARGUMENTS = {'scope': 'read,write,email'}

## GitHub
SOCIAL_AUTH_GITHUB_KEY = '243fa799f9edaf058ce7'
SOCIAL_AUTH_GITHUB_SECRET = 'bb039a7372abb84923889d2ac4a934e98faa76ab'
SOCIAL_AUTH_GITHUB_SCOPE = ['email']

## Google OAuth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '948756394788-77eg6hg3rn12obm3bhnlt58a9h7cds8r.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'S_5VmHYL6NLIUk8kM10cH80y'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
'https://www.googleapis.com/auth/drive',
'https://www.googleapis.com/auth/userinfo.profile'
]