# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServerRegion'
        db.create_table('servers_serverregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
        ))
        db.send_create_signal('servers', ['ServerRegion'])

        # Adding field 'Server.region'
        db.add_column('servers_server', 'region',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['servers.ServerRegion']),
                      keep_default=False)

        # Adding field 'Server.type'
        db.add_column('servers_server', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['servers.ServerType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ServerRegion'
        db.delete_table('servers_serverregion')

        # Deleting field 'Server.region'
        db.delete_column('servers_server', 'region_id')

        # Deleting field 'Server.type'
        db.delete_column('servers_server', 'type_id')


    models = {
        'games.game': {
            'Meta': {'object_name': 'Game'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'allows_fc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_xfer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_factions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_subclasses': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'servers.server': {
            'Meta': {'object_name': 'Server'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.ServerRegion']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servers.ServerType']"})
        },
        'servers.serverregion': {
            'Meta': {'object_name': 'ServerRegion'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'servers.servertype': {
            'Meta': {'object_name': 'ServerType'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['servers']