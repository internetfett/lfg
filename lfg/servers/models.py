from django.db import models
from django.utils.translation import ugettext_lazy as _

from lfg.games.models import Game


class ServerRegion(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=25)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')

    def __unicode__(self):
        return self.name


class ServerType(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=20)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')

    def __unicode__(self):
        return self.name


class ServerTimezone(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=20)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')

    def __unicode__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=50)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    region = models.ForeignKey(ServerRegion, blank=False, verbose_name='region')
    type = models.ForeignKey(ServerType, blank=False, verbose_name='type')
    timezone = models.ForeignKey(ServerTimezone, blank=False, verbose_name='timezone')

    def __unicode__(self):
        return self.name
