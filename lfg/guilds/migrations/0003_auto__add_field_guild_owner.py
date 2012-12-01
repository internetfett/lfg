# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guild.owner'
        db.add_column('guilds_guild', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guild.owner'
        db.delete_column('guilds_guild', 'owner_id')


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
        'guilds.guild': {
            'Meta': {'object_name': 'Guild'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterClass']", 'symmetrical': 'False'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Faction']", 'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'guildtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guilds.GuildType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 26, 0, 0)', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterRole']", 'symmetrical': 'False'}),
            'searchable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.Server']"}),
            'subclasses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['games.CharacterSubclass']", 'symmetrical': 'False'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'guilds.guildplaytime': {
            'Meta': {'object_name': 'GuildPlaytime'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'guild': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guilds.Guild']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'guilds.guildtype': {
            'Meta': {'object_name': 'GuildType'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
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

    complete_apps = ['guilds']