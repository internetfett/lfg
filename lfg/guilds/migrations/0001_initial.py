# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GuildPlaytime'
        db.create_table('guilds_guildplaytime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('guilds', ['GuildPlaytime'])

        # Adding model 'GuildType'
        db.create_table('guilds_guildtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
        ))
        db.send_create_signal('guilds', ['GuildType'])

        # Adding model 'Guild'
        db.create_table('guilds_guild', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servers.Server'])),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Faction'], null=True, blank=True)),
            ('guildtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guilds.GuildType'], null=True, blank=True)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('blurb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 26, 0, 0), blank=True)),
            ('searchable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('guilds', ['Guild'])

        # Adding M2M table for field classes on 'Guild'
        db.create_table('guilds_guild_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guild', models.ForeignKey(orm['guilds.guild'], null=False)),
            ('characterclass', models.ForeignKey(orm['games.characterclass'], null=False))
        ))
        db.create_unique('guilds_guild_classes', ['guild_id', 'characterclass_id'])

        # Adding M2M table for field subclasses on 'Guild'
        db.create_table('guilds_guild_subclasses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guild', models.ForeignKey(orm['guilds.guild'], null=False)),
            ('charactersubclass', models.ForeignKey(orm['games.charactersubclass'], null=False))
        ))
        db.create_unique('guilds_guild_subclasses', ['guild_id', 'charactersubclass_id'])

        # Adding M2M table for field roles on 'Guild'
        db.create_table('guilds_guild_roles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guild', models.ForeignKey(orm['guilds.guild'], null=False)),
            ('characterrole', models.ForeignKey(orm['games.characterrole'], null=False))
        ))
        db.create_unique('guilds_guild_roles', ['guild_id', 'characterrole_id'])

        # Adding M2M table for field playtimes on 'Guild'
        db.create_table('guilds_guild_playtimes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guild', models.ForeignKey(orm['guilds.guild'], null=False)),
            ('guildplaytime', models.ForeignKey(orm['guilds.guildplaytime'], null=False))
        ))
        db.create_unique('guilds_guild_playtimes', ['guild_id', 'guildplaytime_id'])


    def backwards(self, orm):
        # Deleting model 'GuildPlaytime'
        db.delete_table('guilds_guildplaytime')

        # Deleting model 'GuildType'
        db.delete_table('guilds_guildtype')

        # Deleting model 'Guild'
        db.delete_table('guilds_guild')

        # Removing M2M table for field classes on 'Guild'
        db.delete_table('guilds_guild_classes')

        # Removing M2M table for field subclasses on 'Guild'
        db.delete_table('guilds_guild_subclasses')

        # Removing M2M table for field roles on 'Guild'
        db.delete_table('guilds_guild_roles')

        # Removing M2M table for field playtimes on 'Guild'
        db.delete_table('guilds_guild_playtimes')


    models = {
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
            'playtimes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['guilds.GuildPlaytime']", 'symmetrical': 'False'}),
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