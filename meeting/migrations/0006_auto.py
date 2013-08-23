# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field friend_approved on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_friend_approved'))

        # Adding M2M table for field ex_candidate on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_ex_candidate')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])


    def backwards(self, orm):
        # Adding M2M table for field friend_approved on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_friend_approved')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Removing M2M table for field ex_candidate on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_ex_candidate'))


    models = {
        u'meeting.user': {
            'Meta': {'object_name': 'User'},
            'arranger_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'arranger_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_arranger_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_next'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_now': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fk_candidate_now'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'candidate_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chance': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ex_candidate': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fk_ex_candidate'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['meeting.User']"}),
            'fb_email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'friend_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_friendreq'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['meeting.User']"}),
            'friend_ship': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_ship_rel_+'", 'blank': 'True', 'to': u"orm['meeting.User']"}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jointime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'meeting_app': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fk_meeting_app'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['meeting.User']"}),
            'meeting_deny': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fk_meeting_deny'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['meeting.User']"}),
            'meeting_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fk_meeting_req'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['meeting.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'password': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['meeting']