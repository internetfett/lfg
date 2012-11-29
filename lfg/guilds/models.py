from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lfg.games.models import Game, Faction, CharacterClass, CharacterSubclass, CharacterRole
from lfg.servers.models import Server


class GuildType(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=25)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')

    def __unicode__(self):
        return self.name


class Guild(models.Model):
    owner = models.ForeignKey(User, blank=False, verbose_name='owner')
    name = models.CharField(_('name'), blank=False, max_length=35)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    server = models.ForeignKey(Server, blank=False, verbose_name='server')
    faction = models.ForeignKey(Faction, blank=True, null=True, verbose_name='faction')
    guildtype = models.ForeignKey(GuildType, blank=True, null=True, verbose_name='guild focus')
    tagline = models.CharField(_('tagline'), blank=False, max_length=100)
    website = models.CharField(_('website'), blank=True, null=True, max_length=50)
    blurb = models.TextField(_('description'), blank=True, null=True)
    classes = models.ManyToManyField(CharacterClass)
    subclasses = models.ManyToManyField(CharacterSubclass)
    roles = models.ManyToManyField(CharacterRole)
    last_updated = models.DateTimeField(_('last updated'), blank=True, null=False, default=datetime.now())
    searchable = models.BooleanField(_('searchable'), blank=True, null=False, default=1)


class GuildPlaytime(models.Model):
    guild = models.ForeignKey(Guild, blank=False, verbose_name='guild')
    day = models.IntegerField(_('day'), blank=False)
    start_time = models.TimeField(_('start time'), blank=False)
    end_time = models.TimeField(_('end time'), blank=False)

    def __unicode__(self):
        return u'%s %s-%s' % (self.day, self.start_time, self.end_time)
