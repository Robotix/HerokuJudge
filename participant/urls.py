from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^register', 'participant.views.register', name='register'),
    url(r'^(?P<number>\d+)', 'participant.views.info', name='info'),
)
