from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lfg.games.models import Game, Faction, CharacterClass, CharacterSubclass, CharacterRole
from lfg.servers.models import Server


class Player(models.Model):
    owner = models.ForeignKey(User, blank=False, verbose_name='owner')
    name = models.CharField(_('name'), blank=False, max_length=35)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    server = models.ForeignKey(Server, blank=False, verbose_name='server')
    faction = models.ForeignKey(Faction, blank=True, null=True, verbose_name='faction')
    level = models.IntegerField(_('level'), blank=False, max_length=3)
    classes = models.ManyToManyField(CharacterClass)
    subclasses = models.ManyToManyField(CharacterSubclass)
    roles = models.ManyToManyField(CharacterRole)
    blurb = models.TextField(_('description'), blank=True, null=True)
    last_updated = models.DateTimeField(_('last updated'), blank=True, null=False, default=datetime.now())
    searchable = models.BooleanField(_('searchable'), blank=True, null=False, default=1)


class PlayerPlaytime(models.Model):
    Player = models.ForeignKey(Player, blank=False, verbose_name='guild')
    day = models.IntegerField(_('day'), blank=False)
    start_time = models.TimeField(_('start time'), blank=False)
    end_time = models.TimeField(_('end time'), blank=False)

    def __unicode__(self):
        return u'%s %s-%s' % (self.day, self.start_time, self.end_time)
