# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Invite.date_used'
        db.delete_column(u'accounts_invite', 'date_used')

        # Adding field 'Invite.contact_phone'
        db.add_column(u'accounts_invite', 'contact_phone',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=18),
                      keep_default=False)

        # Adding field 'Invite.name'
        db.add_column(u'accounts_invite', 'name',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)

        # Adding field 'Invite.is_active'
        db.add_column(u'accounts_invite', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Invite.email'
        db.alter_column(u'accounts_invite', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=80))

    def backwards(self, orm):
        # Adding field 'Invite.date_used'
        db.add_column(u'accounts_invite', 'date_used',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Invite.contact_phone'
        db.delete_column(u'accounts_invite', 'contact_phone')

        # Deleting field 'Invite.name'
        db.delete_column(u'accounts_invite', 'name')

        # Deleting field 'Invite.is_active'
        db.delete_column(u'accounts_invite', 'is_active')


        # Changing field 'Invite.email'
        db.alter_column(u'accounts_invite', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True))

    models = {
        u'accounts.fexuser': {
            'Meta': {'object_name': 'FexUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'accounts.invite': {
            'Meta': {'object_name': 'Invite'},
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_role': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['accounts']