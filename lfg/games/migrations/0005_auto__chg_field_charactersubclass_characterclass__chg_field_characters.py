# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CharacterSubclass.characterclass'
        db.alter_column('games_charactersubclass', 'characterclass_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.CharacterClass'], null=True))

        # Changing field 'CharacterSubclass.faction'
        db.alter_column('games_charactersubclass', 'faction_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True))

        # Changing field 'CharacterClass.faction'
        db.alter_column('games_characterclass', 'faction_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True))

    def backwards(self, orm):

        # Changing field 'CharacterSubclass.characterclass'
        db.alter_column('games_charactersubclass', 'characterclass_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.CharacterClass']))

        # Changing field 'CharacterSubclass.faction'
        db.alter_column('games_charactersubclass', 'faction_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Faction']))

        # Changing field 'CharacterClass.faction'
        db.alter_column('games_characterclass', 'faction_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Faction']))

    models = {
        'games.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.charactersubclass': {
            'Meta': {'object_name': 'CharacterSubclass'},
            'characterclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.CharacterClass']", 'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
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