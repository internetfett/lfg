# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CharacterClass.faction'
        db.delete_column('games_characterclass', 'faction_id')

        # Adding M2M table for field faction on 'CharacterClass'
        db.create_table('games_characterclass_faction', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('characterclass', models.ForeignKey(orm['games.characterclass'], null=False)),
            ('faction', models.ForeignKey(orm['games.faction'], null=False))
        ))
        db.create_unique('games_characterclass_faction', ['characterclass_id', 'faction_id'])

        # Deleting field 'CharacterRace.faction'
        db.delete_column('games_characterrace', 'faction_id')

        # Adding M2M table for field faction on 'CharacterRace'
        db.create_table('games_characterrace_faction', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('characterrace', models.ForeignKey(orm['games.characterrace'], null=False)),
            ('faction', models.ForeignKey(orm['games.faction'], null=False))
        ))
        db.create_unique('games_characterrace_faction', ['characterrace_id', 'faction_id'])


    def backwards(self, orm):
        # Adding field 'CharacterClass.faction'
        db.add_column('games_characterclass', 'faction',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field faction on 'CharacterClass'
        db.delete_table('games_characterclass_faction')

        # Adding field 'CharacterRace.faction'
        db.add_column('games_characterrace', 'faction',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field faction on 'CharacterRace'
        db.delete_table('games_characterrace_faction')


    models = {
        'games.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
            'faction': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.characterrace': {
            'Meta': {'object_name': 'CharacterRace'},
            'faction': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'games.characterrole': {
            'Meta': {'object_name': 'CharacterRole'},
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
            'race_faction_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_class_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_faction_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['games']