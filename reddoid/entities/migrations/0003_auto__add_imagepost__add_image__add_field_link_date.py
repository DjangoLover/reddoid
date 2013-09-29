# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImagePost'
        db.create_table(u'entities_imagepost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entities.Image'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Post'])),
        ))
        db.send_create_signal(u'entities', ['ImagePost'])

        # Adding model 'Image'
        db.create_table(u'entities_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'entities', ['Image'])

        # Adding field 'Link.date'
        db.add_column(u'entities_link', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 29, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ImagePost'
        db.delete_table(u'entities_imagepost')

        # Deleting model 'Image'
        db.delete_table(u'entities_image')

        # Deleting field 'Link.date'
        db.delete_column(u'entities_link', 'date')


    models = {
        u'entities.image': {
            'Meta': {'object_name': 'Image'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'entities.imagepost': {
            'Meta': {'object_name': 'ImagePost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entities.Image']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Post']"})
        },
        u'entities.link': {
            'Meta': {'object_name': 'Link'},
            'date': ('django.db.models.fields.DateField', [], {}),
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