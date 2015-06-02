from django.forms import widgets
from rest_framework import serializers
from actors.models import Node, Deployment, ConfigurationSequence, SensorMap, Sensor, Reading, Statistics

class NodeSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # node_id = serializers.IntegerField(required=True, allow_blank=False)
    
    class Meta:
            model = Node
            fields = ('id', 'node_id')

    def create(self, validated_data):
        """
        Create and return a new `Node` instance, given the validated data.
        """
        return Node.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Node` instance, given the validated data.
        """
        instance.node_id = validated_data.get('node_id', instance.node_id)
        instance.save()
        return instance

class DeploymentSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # cluster = serializers.CharField(required=False, allow_blank=True, max_length=128)
    # location = serializers.CharField(required=False, allow_blank=True, max_length=128)
 
    class Meta:
            model = Deployment
            fields = ('id', 'name', 'code', 'cluster', 'location')

    def create(self, validated_data):
        """
        Create and return a new `Deployment` instance, given the validated data.
        """
        return Deployment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Deployment` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.cluster = validated_data.get('cluster', instance.cluster)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

class ConfigSeqSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # type_id = serializers.IntegerField(required=True, allow_blank=False)
    # ip_address = serializers.CharField(required=False, allow_blank=True, max_length=128)
    # gateway_ip = serializers.CharField(required=False, allow_blank=True, max_length=128)
    # node_profile_type = serializers.ChoiceField(choices=NODE_CHOICES, default=SENSOR_NODE)

    class Meta:
            model = ConfigurationSequence
            fields = ('id', 'type_id', 'ip_address', 'gateway_ip', 'node_profile_type')

    def create(self, validated_data):
        """
        Create and return a new `ConfigurationSequence` instance, given the validated data.
        """
        return ConfigurationSequence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ConfigurationSequence` instance, given the validated data.
        """
        instance.type_id = validated_data.get('type_id', instance.type_id)
        instance.ip_address = validated_data.get('ip_address', instance.ip_address)
        instance.gateway_ip = validated_data.get('gateway_ip', instance.gateway_ip)
        instance.node_profile_type = validated_data.get('node_profile_type', instance.node_profile_type)
        instance.save()
        return instance

class SensorMapSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # bit_position = serializers.IntegerField(required=True, allow_blank=False)

    class Meta:
            model = SensorMap
            fields = ('id', 'bit_position')

    def create(self, validated_data):
        """
        Create and return a new `SensorMap` instance, given the validated data.
        """
        return SensorMap.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `SensorMap` instance, given the validated data.
        """
        instance.bit_position = validated_data.get('bit_position', instance.bit_position)
        instance.save()
        return instance

class SensorSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # modality = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # data_length = serializers.IntegerField(required=True, allow_blank=False)
    # data_api_name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # product_model = serializers.CharField(required=False, allow_blank=True, max_length=128)
    # sensing_interval = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
            model = Sensor
            fields = ('id', 'name', 'modality', 'data_length', 'data_api_name', 'product_model', 'sensing_interval')

    def create(self, validated_data):
        """
        Create and return a new `Sensor` instance, given the validated data.
        """
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Sensor` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.modality = validated_data.get('modality', instance.modality)
        instance.data_length = validated_data.get('data_length', instance.data_length)
        instance.data_api_name = validated_data.get('data_api_name', instance.data_api_name)
        instance.product_model = validated_data.get('product_model', instance.product_model)
        instance.sensing_interval = validated_data.get('sensing_interval', instance.sensing_interval)
        instance.save()
        return instance

class ReadingSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # timestamp = serializers.DateTimeField(read_only=True)
    # gwtimestamp = serializers.DateTimeField()
    # value = serializers.CharField(required=True, allow_blank=False, max_length=50)
    # tag = serializers.CharField(required=False, allow_blank=True, max_length=50)

    class Meta:
            model = Reading
            fields = ('id', 'timestamp', 'gwtimestamp', 'value', 'tag')

    def create(self, validated_data):
        """
        Create and return a new `Reading` instance, given the validated data.
        """
        return Reading.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Reading` instance, given the validated data.
        """
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.gwtimestamp = validated_data.get('gwtimestamp', instance.gwtimestamp)
        instance.value = validated_data.get('value', instance.value)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance

class StatisticsSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # modality = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # data_length = serializers.IntegerField(required=True, allow_blank=False)
    # data_api_name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    # sensing_interval = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
            model = Reading
            fields = ('id', 'name', 'modality', 'data_length', 'data_api_name', 'sensing_interval')

    def create(self, validated_data):
        """
        Create and return a new `Statistics` instance, given the validated data.
        """
        return Statistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Statistics` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.modality = validated_data.get('modality', instance.modality)
        instance.data_length = validated_data.get('data_length', instance.data_length)
        instance.data_api_name = validated_data.get('data_api_name', instance.data_api_name)
        instance.sensing_interval = validated_data.get('sensing_interval', instance.sensing_interval)
        instance.save()
        return instance