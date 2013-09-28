# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'entities_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'entities', ['Link'])

        # Adding model 'LinkPost'
        db.create_table(u'entities_linkpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entities.Link'])),
            ('Post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Post'])),
        ))
        db.send_create_signal(u'entities', ['LinkPost'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'entities_link')

        # Deleting model 'LinkPost'
        db.delete_table(u'entities_linkpost')


    models = {
        u'entities.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'entities.linkpost': {
            'Meta': {'object_name': 'LinkPost'},
            'Post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Post']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entities.Link']"})
        },
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
        }
    }

    complete_apps = ['entities']