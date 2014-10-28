from django.conf.urls import patterns, include, url
from testproject.views import status_false, homePage, submit, result, AuthComplete, LoginError 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^result/$', result),
    url(r'^status/fail$', status_false),
    url(r'^$',homePage),
    url(r'^submit/$',submit),
    url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
     url(r'^login-error/$', LoginError.as_view()),
    url(r'', include('social_auth.urls')),
)
