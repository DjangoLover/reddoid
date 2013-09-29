# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.votes_count'
        db.add_column(u'entities_image', 'votes_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.votes_count'
        db.delete_column(u'entities_image', 'votes_count')


    models = {
        u'entities.image': {
            'Meta': {'object_name': 'Image'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'entities.imagepost': {
            'Meta': {'object_name': 'ImagePost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entities.Image']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Post']"})
        },
        u'entities.link': {
            'Meta': {'ordering': "('-votes_count',)", 'object_name': 'Link'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'entities.linkpost': {
            'Meta': {'object_name': 'LinkPost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entities.Link']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Post']"})
        },
        u'sources.post': {
            'Meta': {'object_name': 'Post'},
            'api_content': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {}),
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