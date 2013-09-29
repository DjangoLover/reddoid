# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkVote'
        db.create_table(u'votes_linkvote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', to=orm['entities.Link'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='link_votes', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'votes', ['LinkVote'])

        # Adding model 'ImageVote'
        db.create_table(u'votes_imagevote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', to=orm['entities.Image'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image_votes', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'votes', ['ImageVote'])


    def backwards(self, orm):
        # Deleting model 'LinkVote'
        db.delete_table(u'votes_linkvote')

        # Deleting model 'ImageVote'
        db.delete_table(u'votes_imagevote')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entities.image': {
            'Meta': {'object_name': 'Image'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'entities.link': {
            'Meta': {'object_name': 'Link'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'votes.imagevote': {
            'Meta': {'object_name': 'ImageVote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': u"orm['entities.Image']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_votes'", 'to': u"orm['auth.User']"})
        },
        u'votes.linkvote': {
            'Meta': {'object_name': 'LinkVote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': u"orm['entities.Link']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'link_votes'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['votes']