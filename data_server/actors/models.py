from django.db import models
from django.utils import timezone

class Node(models.Model):
    ''' Node Related Information
    '''
    node_id = models.IntegerField('Node ID', blank=False)

    conf_seq = models.ForeignKey('ConfigurationSequence', blank=False, null=False,
                        related_name='node')

    deployment = models.ForeignKey('Deployment', blank=False, null=False,
                        related_name='node')

    # owner = models.ForeignKey('auth.User', blank=True,  null=True, related_name='node')

    def __str__(self):
        return ', '.join([str(self.node_id)])


class Deployment(models.Model):
    ''' Deployment Information
    '''

    name = models.CharField(max_length=128, blank=False)

    cluster = models.CharField(max_length=128, blank=True)

    location = models.CharField(max_length=128, blank=True)

    # owner = models.ForeignKey('auth.User', blank=True, null=True, related_name='deployment')

    def __str__(self):
        return ', '.join([str(self.id), self.name, self.cluster, self.location])


class ConfigurationSequence(models.Model):
    ''' Configuration Sequence Information
    '''
    GATEWAY_NODE, SENSOR_NODE = range(2)
    NODE_CHOICES = (
            (GATEWAY_NODE, 'GatewayNode'),
            (SENSOR_NODE, 'SensorNode')
        )

    type_id = models.PositiveSmallIntegerField('Node Type', blank=False)

    ip_address = models.CharField(max_length=128, blank=True)

    gateway_ip = models.CharField(max_length=128, blank=True)    

    node_profile_type = models.PositiveSmallIntegerField(
                 default=SENSOR_NODE,
                 choices=NODE_CHOICES
            )

    def __str__(self):
        return ', '.join(['type ' + str(self.type_id), 
                        self.get_node_profile_type_display()])


class SensorMap(models.Model):
    ''' Sensor Map Information
    '''
    bit_position = models.PositiveSmallIntegerField('Bit Position', blank=False)

    conf_seq = models.ForeignKey('ConfigurationSequence', blank=False, null=False,
                        related_name='sensor_map')

    sensor = models.ForeignKey('Sensor', blank=False, null=False,
                        related_name='sensor_map')

    def __str__(self):
        return ', '.join(['config_id-' + str(self.conf_seq), 'bit-' + 
                str(self.bit_position), self.sensor.modality])
   

class Sensor(models.Model):
    ''' Sensor Related Information
    '''
    
    name = models.CharField(max_length=128, blank=False)

    modality = models.CharField(max_length=128, blank=False)
            
    data_length = models.PositiveIntegerField('data length', blank=False)

    data_api_name = models.CharField(max_length=128, blank=False)

    product_model = models.CharField(max_length=128)

    sensing_interval = models.PositiveIntegerField()

    def __str__(self):
        return ', '.join([self.modality, str(self.data_length)])


class Reading(models.Model):
    ''' Sensor Readings
    '''

    timestamp = models.DateTimeField(auto_now=True, default=timezone.now())

    gwtimestamp = models.DateTimeField(default=timezone.now())

    sequence = models.PositiveIntegerField()

    node = models.ForeignKey('Node', blank=False, null=False,
                        related_name='sensor_reading')

    sensor = models.ForeignKey('Sensor', blank=False, null=False,
                        related_name='sensor_reading')

    value = models.CharField(max_length=50)

    tag = models.CharField(max_length=50)

    #objects = managers.ReadingsManager()

    def __str__(self):
        return ', '.join([str(self.id), str(self.node.node_id), str(self.timestamp), self.value])

class Statistics(models.Model):
    ''' Stats Related Information
    '''
    
    name = models.CharField(max_length=128, blank=False)

    modality = models.CharField(max_length=128, blank=False)
            
    data_length = models.PositiveIntegerField('data length')

    data_api_name = models.CharField(max_length=128, blank=False)

    sensing_interval = models.PositiveIntegerField()

    def __str__(self):
        return ', '.join([self.modality, str(data_length)])
