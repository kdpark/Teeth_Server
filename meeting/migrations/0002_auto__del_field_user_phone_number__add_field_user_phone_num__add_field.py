# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.phone_number'
        db.delete_column(u'meeting_user', 'phone_number')

        # Adding field 'User.phone_num'
        db.add_column(u'meeting_user', 'phone_num',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.done'
        db.add_column(u'meeting_user', 'done',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'User.candidate_num'
        db.add_column(u'meeting_user', 'candidate_num',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.friend_num'
        db.add_column(u'meeting_user', 'friend_num',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.arranger_now'
        db.add_column(u'meeting_user', 'arranger_now',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fk_arranger_now', null=True, to=orm['meeting.User']),
                      keep_default=False)

        # Adding field 'User.candidate_now'
        db.add_column(u'meeting_user', 'candidate_now',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fk_candidate_now', null=True, to=orm['meeting.User']),
                      keep_default=False)

        # Adding field 'User.arranger_next'
        db.add_column(u'meeting_user', 'arranger_next',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fk_arranger_next', null=True, to=orm['meeting.User']),
                      keep_default=False)

        # Adding field 'User.candidate_next'
        db.add_column(u'meeting_user', 'candidate_next',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fk_candidate_next', null=True, to=orm['meeting.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.phone_number'
        db.add_column(u'meeting_user', 'phone_number',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'User.phone_num'
        db.delete_column(u'meeting_user', 'phone_num')

        # Deleting field 'User.done'
        db.delete_column(u'meeting_user', 'done')

        # Deleting field 'User.candidate_num'
        db.delete_column(u'meeting_user', 'candidate_num')

        # Deleting field 'User.friend_num'
        db.delete_column(u'meeting_user', 'friend_num')

        # Deleting field 'User.arranger_now'
        db.delete_column(u'meeting_user', 'arranger_now_id')

        # Deleting field 'User.candidate_now'
        db.delete_column(u'meeting_user', 'candidate_now_id')

        # Deleting field 'User.arranger_next'
        db.delete_column(u'meeting_user', 'arranger_next_id')

        # Deleting field 'User.candidate_next'
        db.delete_column(u'meeting_user', 'candidate_next_id')


    models = {
        u'meeting.user': {
            'Meta': {'object_name': 'User'},
            'arranger_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'arranger_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'done': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'friend_approved': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friend_approved_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'friend_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'friend_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friend_req_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'friend_ship': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_ship_rel_+'", 'blank': 'True', 'to': u"orm['meeting.User']"}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jointime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'meeting_app': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_app_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_deny': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_deny_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_req_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'password': ('django.db.models.fields.TextField', [], {}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['meeting']