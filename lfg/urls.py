from django.conf.urls import patterns, include, url
from django.contrib import admin

from lfg.guilds.views import CreateGuildView, DeleteGuildView, UpdateGuildView, GuildDetailView
from lfg.players.views import CreatePlayerView, DeletePlayerView, UpdatePlayerView, PlayerDetailView
from lfg.views import HomepageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^guilds/(?P<pk>\d+)/$', GuildDetailView.as_view(), name='guild_detail'),
    url(r'^guilds/create/$', CreateGuildView.as_view(), name='create_guild'),
    url(r'^guilds/delete/(?P<pk>\d+)/$', DeleteGuildView.as_view(), name='delete_guild'),
    url(r'^guilds/update/(?P<pk>\d+)/$', UpdateGuildView.as_view(), name='update_guild'),
    url(r'^players/(?P<pk>\d+)/$', PlayerDetailView.as_view(), name='player_detail'),
    url(r'^players/create/$', CreatePlayerView.as_view(), name='create_player'),
    url(r'^players/delete/(?P<pk>\d+)/$', DeletePlayerView.as_view(), name='delete_player'),
    url(r'^players/update/(?P<pk>\d+)/$', UpdatePlayerView.as_view(), name='update_player'),
)
