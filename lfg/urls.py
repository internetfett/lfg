from django.conf.urls import patterns, include, url
from lfg.views import HomepageView
from lfg.guilds.views import CreateGuildView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^guilds/create/$', CreateGuildView.as_view(), name='create_guild'),
)
