from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
	url(r'^$', 'myAccountPage', name='myAccountPage'),
	url(r'^(?P<user_name>\w+)', 'AccountPage', name='AccountPage'),
)
