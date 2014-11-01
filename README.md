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

Install psycopg2 using "pip install psycopg2" and configure it using the above settings.
Run "python manage.py syncdb" to sync the local database.
The local server should now run without any errors.

