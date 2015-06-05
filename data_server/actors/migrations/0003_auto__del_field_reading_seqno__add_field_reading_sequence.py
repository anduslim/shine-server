# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reading.seqno'
        db.delete_column('actors_reading', 'seqno')

        # Adding field 'Reading.sequence'
        db.add_column('actors_reading', 'sequence',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Reading.seqno'
        db.add_column('actors_reading', 'seqno',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Reading.sequence'
        db.delete_column('actors_reading', 'sequence')


    models = {
        'actors.configurationsequence': {
            'Meta': {'object_name': 'ConfigurationSequence'},
            'gateway_ip': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'node_profile_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'type_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'actors.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'cluster': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'actors.node': {
            'Meta': {'object_name': 'Node'},
            'conf_seq': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node'", 'to': "orm['actors.ConfigurationSequence']"}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node'", 'to': "orm['actors.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'actors.reading': {
            'Meta': {'object_name': 'Reading'},
            'gwtimestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 5, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_reading'", 'to': "orm['actors.Node']"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_reading'", 'to': "orm['actors.Sensor']"}),
            'sequence': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'default': 'datetime.datetime(2015, 6, 5, 0, 0)'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'actors.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'data_api_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'data_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'product_model': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sensing_interval': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'actors.sensormap': {
            'Meta': {'object_name': 'SensorMap'},
            'bit_position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'conf_seq': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_map'", 'to': "orm['actors.ConfigurationSequence']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_map'", 'to': "orm['actors.Sensor']"})
        },
        'actors.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'data_api_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'data_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sensing_interval': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['actors']