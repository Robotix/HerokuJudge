from django.conf.urls import patterns, include, url
from testproject.views import status_false, homePage, submit, result, landingPage 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^result/$', result),
    url(r'^status/fail$', status_false),
    url(r'^$',homePage),
    url(r'^submit/$',submit),
    url(r'^landingPage/$',landingPage),
    url(r'', include('social_auth.urls')),
)
