from django.conf.urls import patterns, include, url
from ojMON.views import status_false, submitPage, submit, result 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ojMON.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^result/$', result),
    url(r'^status/fail$', status_false),
    url(r'^$',submitPage),
    url(r'^submit/$',submit),
)
