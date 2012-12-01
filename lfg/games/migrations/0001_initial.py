# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('games_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('has_factions', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_subclasses', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allows_xfer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allows_fc', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('games', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('games_game')


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
        }
    }

    complete_apps = ['games']