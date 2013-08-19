# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'meeting_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('password', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('profile_pic', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('jointime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'meeting', ['User'])

        # Adding M2M table for field friend_ship on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_friend_ship')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field friend_req on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_friend_req')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field friend_approved on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_friend_approved')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field meeting_req on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_meeting_req')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field meeting_app on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_meeting_app')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field meeting_deny on 'User'
        m2m_table_name = db.shorten_name(u'meeting_user_meeting_deny')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'meeting.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'meeting.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'meeting_user')

        # Removing M2M table for field friend_ship on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_friend_ship'))

        # Removing M2M table for field friend_req on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_friend_req'))

        # Removing M2M table for field friend_approved on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_friend_approved'))

        # Removing M2M table for field meeting_req on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_meeting_req'))

        # Removing M2M table for field meeting_app on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_meeting_app'))

        # Removing M2M table for field meeting_deny on 'User'
        db.delete_table(db.shorten_name(u'meeting_user_meeting_deny'))


    models = {
        u'meeting.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'friend_approved': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_approved_rel_+'", 'blank': "'True'", 'to': u"orm['meeting.User']"}),
            'friend_req': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_req_rel_+'", 'blank': "'True'", 'to': u"orm['meeting.User']"}),
            'friend_ship': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': "'True'", 'related_name': "'friend_ship_rel_+'", 'blank': "'True'", 'to': u"orm['meeting.User']"}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jointime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'meeting_app': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_app_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_deny': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_deny_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'meeting_req': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meeting_req_rel_+'", 'null': 'True', 'to': u"orm['meeting.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'password': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['meeting']