from django.db import models
from django.utils.translation import ugettext_lazy as _

class Game(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=50)
    abbr = models.CharField(_('abbreviation'), blank=False, max_length=10)
    class_name = models.CharField(_('class name'), blank=True, null=True, max_length=25)
    subclass_name = models.CharField(_('subclass name'), blank=True, null=True, max_length=25)
    has_factions = models.BooleanField(_('has factions'))
    has_subclasses = models.BooleanField(_('has subclasses'))
    subclass_class_based = models.BooleanField(_('subclasses are class based'))
    subclass_faction_based = models.BooleanField(_('subclasses are faction based'))
    race_faction_based = models.BooleanField(_('races are faction based'))
    allows_xfer = models.BooleanField(_('allows server transfer'))
    allows_fc = models.BooleanField(_('allows faction change'))
    
    def __unicode__(self):
        return self.name
        
class Faction(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=30)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    
    def __unicode__(self):
        return self.name

class CharacterClass(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=30)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    faction = models.ManyToManyField(Faction, blank=True, null=True, verbose_name='faction')
    
    def __unicode__(self):
        return self.name
        
class CharacterSubclass(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=30)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    faction = models.ForeignKey(Faction, blank=True, null=True, verbose_name='faction')
    characterclass = models.ForeignKey(CharacterClass, blank=True, null=True, verbose_name='character class')
    
    def __unicode__(self):
        return self.name

class CharacterRole(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=30)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    
    def __unicode__(self):
        return self.name
        
class CharacterRace(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=30)
    game = models.ForeignKey(Game, blank=False, verbose_name='game')
    faction = models.ManyToManyField(Faction, blank=True, null=True, verbose_name='faction')
    
    def __unicode__(self):
        return self.name
