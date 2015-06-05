from django.forms import widgets
from rest_framework import serializers
from actors.models import Node, Deployment, ConfigurationSequence, SensorMap, Sensor, Reading, Statistics


class NodeSerializer(serializers.ModelSerializer):
    #deployment = serializers.CharField(source='deployment.name')
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
            model = Node
            fields = ('id', 'node_id', 'conf_seq', 'deployment') #, 'owner')


class DeploymentSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
            model = Deployment
            fields = ('id', 'name', 'cluster', 'location') #, 'owner')


class ConfigSeqSerializer(serializers.ModelSerializer):

    class Meta:
            model = ConfigurationSequence
            fields = ('id', 'type_id', 'ip_address', 'gateway_ip', 'node_profile_type')


class SensorMapSerializer(serializers.ModelSerializer):

    class Meta:
            model = SensorMap
            fields = ('id', 'bit_position', 'conf_seq', 'sensor')


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
            model = Sensor
            fields = ('id', 'name', 'modality', 'data_length', 'data_api_name', 'product_model', 'sensing_interval')


class ReadingSerializer(serializers.ModelSerializer):

    class Meta:
            model = Reading
            fields = ('id', 'timestamp', 'gwtimestamp', 'node', 'sensor', 'value', 'tag', 'sequence')


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
            model = Statistics
            fields = ('id', 'name', 'modality', 'data_length', 'data_api_name', 'sensing_interval')
