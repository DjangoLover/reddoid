# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'sources_post', (
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=120, primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Source'])),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('api_content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sources', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'sources_post')


    models = {
        u'sources.post': {
            'Meta': {'object_name': 'Post'},
            'api_content': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '120', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Source']"})
        },
        u'sources.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sources.sourceslist': {
            'Meta': {'object_name': 'SourcesList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sources']