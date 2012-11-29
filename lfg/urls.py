from django.conf.urls import patterns, include, url
from django.contrib import admin

from lfg.guilds.views import CreateGuildView
from lfg.views import HomepageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^guilds/create/$', CreateGuildView.as_view(), name='create_guild'),
)
