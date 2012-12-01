# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('players_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servers.Server'])),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('blurb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 26, 0, 0), blank=True)),
            ('searchable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('players', ['Player'])

        # Adding M2M table for field classes on 'Player'
        db.create_table('players_player_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['players.player'], null=False)),
            ('characterclass', models.ForeignKey(orm['games.characterclass'], null=False))
        ))
        db.create_unique('players_player_classes', ['player_id', 'characterclass_id'])

        # Adding M2M table for field subclasses on 'Player'
        db.create_table('players_player_subclasses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['players.player'], null=False)),
            ('charactersubclass', models.ForeignKey(orm['games.charactersubclass'], null=False))
        ))
        db.create_unique('players_player_subclasses', ['player_id', 'charactersubclass_id'])

        # Adding M2M table for field roles on 'Player'
        db.create_table('players_player_roles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['players.player'], null=False)),
            ('characterrole', models.ForeignKey(orm['games.characterrole'], null=False))
        ))
        db.create_unique('players_player_roles', ['player_id', 'characterrole_id'])

        # Adding model 'PlayerPlaytime'
        db.create_table('players_playerplaytime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['players.Player'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('players', ['PlayerPlaytime'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('players_player')

        # Removing M2M table for field classes on 'Player'
        db.delete_table('players_player_classes')

        # Removing M2M table for field subclasses on 'Player'
        db.delete_table('players_player_subclasses')

        # Removing M2M table for field roles on 'Player'
        db.delete_table('players_player_roles')

        # Deleting model 'PlayerPlaytime'
        db.delete_table('players_playerplaytime')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'games.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
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
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'has_factions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_subclasses': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'race_faction_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_class_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_faction_based': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subclass_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        'players.player': {
            'Meta': {'object_name': 'Player'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterClass']", 'symmetrical': 'False'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 26, 0, 0)', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterRole']", 'symmetrical': 'False'}),
            'searchable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.Server']"}),
            'subclasses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterSubclass']", 'symmetrical': 'False'})
        },
        'players.playerplaytime': {
            'Meta': {'object_name': 'PlayerPlaytime'},
            'Player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Player']"}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'servers.server': {
            'Meta': {'object_name': 'Server'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.ServerRegion']"}),
            'timezone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.ServerTimezone']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.ServerType']"})
        },
        'servers.serverregion': {
            'Meta': {'object_name': 'ServerRegion'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'servers.servertimezone': {
            'Meta': {'object_name': 'ServerTimezone'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'servers.servertype': {
            'Meta': {'object_name': 'ServerType'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['players']