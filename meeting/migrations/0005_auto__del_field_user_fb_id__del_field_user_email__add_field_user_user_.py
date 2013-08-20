# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.fb_id'
        db.delete_column(u'meeting_user', 'fb_id')

        # Deleting field 'User.email'
        db.delete_column(u'meeting_user', 'email')

        # Adding field 'User.user_id'
        db.add_column(u'meeting_user', 'user_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=40),
                      keep_default=False)

        # Adding field 'User.fb_email'
        db.add_column(u'meeting_user', 'fb_email',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


        # Changing field 'User.password'
        db.alter_column(u'meeting_user', 'password', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Adding field 'User.fb_id'
        db.add_column(u'meeting_user', 'fb_id',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.email'
        db.add_column(u'meeting_user', 'email',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=40, unique=True),
                      keep_default=False)

        # Deleting field 'User.user_id'
        db.delete_column(u'meeting_user', 'user_id')

        # Deleting field 'User.fb_email'
        db.delete_column(u'meeting_user', 'fb_email')


        # Changing field 'User.password'
        db.alter_column(u'meeting_user', 'password', self.gf('django.db.models.fields.TextField')(default=1))

    models = {
        u'meeting.user': {
            'Meta': {'object_name': 'User'},
            'arranger_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'arranger_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chance': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fb_email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'friend_approved': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friend_approved_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'friend_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friend_req_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'friend_ship': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_ship_rel_+'", 'blank': 'True', 'to': u"orm['meeting.User']"}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jointime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'meeting_app': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_app_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_deny': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_deny_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_req_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'password': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['meeting']