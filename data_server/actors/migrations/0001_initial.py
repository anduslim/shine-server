# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table('actors_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')()),
            ('conf_seq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.ConfigurationSequence'], related_name='node')),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.Deployment'], related_name='node')),
        ))
        db.send_create_signal('actors', ['Node'])

        # Adding model 'Deployment'
        db.create_table('actors_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cluster', self.gf('django.db.models.fields.CharField')(blank=True, max_length=128)),
            ('location', self.gf('django.db.models.fields.CharField')(blank=True, max_length=128)),
        ))
        db.send_create_signal('actors', ['Deployment'])

        # Adding model 'ConfigurationSequence'
        db.create_table('actors_configurationsequence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ip_address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=128)),
            ('gateway_ip', self.gf('django.db.models.fields.CharField')(blank=True, max_length=128)),
            ('node_profile_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal('actors', ['ConfigurationSequence'])

        # Adding model 'SensorMap'
        db.create_table('actors_sensormap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bit_position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('conf_seq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.ConfigurationSequence'], related_name='sensor_map')),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.Sensor'], related_name='sensor_map')),
        ))
        db.send_create_signal('actors', ['SensorMap'])

        # Adding model 'Sensor'
        db.create_table('actors_sensor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('modality', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('data_length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('data_api_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('product_model', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sensing_interval', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('actors', ['Sensor'])

        # Adding model 'Reading'
        db.create_table('actors_reading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True, default=datetime.datetime(2015, 5, 27, 0, 0))),
            ('gwtimestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 5, 27, 0, 0))),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.Node'], related_name='sensor_reading')),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.Sensor'], related_name='sensor_reading')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('actors', ['Reading'])

        # Adding model 'Statistics'
        db.create_table('actors_statistics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('modality', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('data_length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('data_api_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sensing_interval', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('actors', ['Statistics'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table('actors_node')

        # Deleting model 'Deployment'
        db.delete_table('actors_deployment')

        # Deleting model 'ConfigurationSequence'
        db.delete_table('actors_configurationsequence')

        # Deleting model 'SensorMap'
        db.delete_table('actors_sensormap')

        # Deleting model 'Sensor'
        db.delete_table('actors_sensor')

        # Deleting model 'Reading'
        db.delete_table('actors_reading')

        # Deleting model 'Statistics'
        db.delete_table('actors_statistics')


    models = {
        'actors.configurationsequence': {
            'Meta': {'object_name': 'ConfigurationSequence'},
            'gateway_ip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'node_profile_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'type_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'actors.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'cluster': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'actors.node': {
            'Meta': {'object_name': 'Node'},
            'conf_seq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.ConfigurationSequence']", 'related_name': "'node'"}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.Deployment']", 'related_name': "'node'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'actors.reading': {
            'Meta': {'object_name': 'Reading'},
            'gwtimestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 5, 27, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.Node']", 'related_name': "'sensor_reading'"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.Sensor']", 'related_name': "'sensor_reading'"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True', 'default': 'datetime.datetime(2015, 5, 27, 0, 0)'}),
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
            'conf_seq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.ConfigurationSequence']", 'related_name': "'sensor_map'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actors.Sensor']", 'related_name': "'sensor_map'"})
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