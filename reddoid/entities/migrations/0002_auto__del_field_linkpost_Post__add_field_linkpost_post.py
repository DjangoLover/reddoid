# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'LinkPost.Post'
        db.delete_column(u'entities_linkpost', 'Post_id')

        # Adding field 'LinkPost.post'
        db.add_column(u'entities_linkpost', 'post',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sources.Post']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'LinkPost.Post'
        raise RuntimeError("Cannot reverse this migration. 'LinkPost.Post' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'LinkPost.Post'
        db.add_column(u'entities_linkpost', 'Post',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Post']),
                      keep_default=False)

        # Deleting field 'LinkPost.post'
        db.delete_column(u'entities_linkpost', 'post_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entities.Link']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Post']"})
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