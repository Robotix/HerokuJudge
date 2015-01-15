from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sudocode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sudocode.views.index', name='index'),
    url(r'^dashboard', 'sudocode.views.dashboard', name='dashboard'),
    url(r'^theraidone', 'sudocode.views.theraidone', name='theraidone'),
    url(r'^theraidtwo', 'sudocode.views.theraidtwo', name='theraidtwo'),
    url(r'^logout', 'sudocode.views.logout', name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^pygments/', include('django_pygments.urls', namespace='pygments')),
    url(r'^submission/', include('submission.urls', namespace='submission')),
    url(r'^user/', include('users.urls', namespace='users')),
    url(r'^submit/', 'sudocode.views.submit', name='submit'),
    url(r'^status/(?P<uniqueID>\d+)', 'sudocode.views.status', name='status'),
)

