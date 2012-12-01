# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CharacterSublass'
        db.create_table('games_charactersublass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], blank=True)),
            ('characterclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.CharacterClass'], blank=True)),
        ))
        db.send_create_signal('games', ['CharacterSublass'])


    def backwards(self, orm):
        # Deleting model 'CharacterSublass'
        db.delete_table('games_charactersublass')


    models = {
        'games.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.charactersublass': {
            'Meta': {'object_name': 'CharacterSublass'},
            'characterclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.CharacterClass']", 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.faction': {
            'Meta': {'object_name': 'Faction'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.game': {
            'Meta': {'object_name': 'Game'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'allows_fc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_xfer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_factions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_subclasses': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subclass_class_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_faction_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['games']