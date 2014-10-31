heroku_app
==========

To run locally, change database settings in /ojMON/testproject/settings.py

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'postgres',
		'USER': 'robotix2014',
		'PASSWORD': 'robotix2014',
		'HOST': 'localhost',
		'PORT': '5432'
	}
}