from django.conf.urls import patterns, include, url
from testproject.views import status_false, homePage, submit, result, landingPage, raid1, raid2

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^result/$', result),
    url(r'^status/fail$', status_false),
    url(r'^$',homePage),
    url(r'^submit/$',submit),
    url(r'^landingPage/$',landingPage),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^leaderboard/$',leaderboard),
    url(r'^raid1/$',raid1),
    url(r'^raid2/$',raid2),
)
