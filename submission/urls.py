from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^(?P<uniqueID>\d+)/$', 'submission.views.submission', name='submission'),
)
