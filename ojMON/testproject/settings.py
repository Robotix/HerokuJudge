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
    BASE_DIR+'/templates/',
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
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'social.backends.github.GithubOAuth2',
   'social.backends.disqus.DisqusOAuth2',
   'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_FACEBOOK_KEY            = '596534703784377'
SOCIAL_AUTH_FACEBOOK_SECRET         = '80584bb5bf55d84bd8d61f9b2e7ffd62'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY       = '948756394788-hq2uule75a585h7ivk7raei301dppiah.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET    = '-xfOIxciKMxPiH-KSjZYlg6o '

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_GITHUB_KEY = '243fa799f9edaf058ce7'
SOCIAL_AUTH_GITHUB_SECRET = 'bb039a7372abb84923889d2ac4a934e98faa76ab'
SOCIAL_AUTH_GITHUB_SCOPE = ['email']

SOCIAL_AUTH_DISQUS_KEY = '89Jtc2FY2hNbvIabTZ0UH6kdVOJ1Pf9OHZeel4DIiG4y8aD9vBNm3RNngRimBTo8'
SOCIAL_AUTH_DISQUS_SECRET = 'Bn5rDKBqrEvJ7N0kOKP4udotAz3Y4g1NXY5oNdUpFaKRWtJfekbKMPufTfkUcU4k'
SOCIAL_AUTH_DISQUS_AUTH_EXTRA_ARGUMENTS = {'scope': 'read,write,email'}

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/landingPage'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da4abl57es557h',
        'USER': 'xeujnnexbxwkde',
        'PASSWORD': 'dEieJrTwnUA9zsNSdfRDoUmBnh',
        'HOST': 'ec2-54-204-40-140.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

# DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'postgres', 'USER': 'robotix2014', 'PASSWORD': 'robotix2014', 'HOST': 'localhost', 'PORT': '5432' } }

# Internationalization
# https://docs.djan,goproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/templates/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "templates"),
    '/var/www/templates/',
)
