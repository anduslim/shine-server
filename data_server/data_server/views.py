
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from actors.models import Deployment, Node, ConfigurationSequence, SensorMap, Sensor, Reading, Statistics
from data_server.serializers import DeploymentSerializer, NodeSerializer, ConfigSeqSerializer, SensorMapSerializer, SensorSerializer, ReadingSerializer, StatisticsSerializer


class DeploymentList(generics.ListCreateAPIView):
    """
    List all deployments, or create a new deployment.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer

class DeploymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a deployment instance.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


class NodeList(generics.ListCreateAPIView):
    """
    List all nodes, or create a new node.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a node instance.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class ConfSeqList(generics.ListCreateAPIView):
    """
    List all configurationsequences, or create a new configurationsequence.
    """
    queryset = ConfigurationSequence.objects.all()
    serializer_class = ConfigSeqSerializer

class ConfSeqDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a configurationsequence instance.
    """
    queryset = ConfigurationSequence.objects.all()
    serializer_class = ConfigSeqSerializer


class SensorMapList(generics.ListCreateAPIView):
    """
    List all sensor maps, or create a new sensor map.
    """
    queryset = SensorMap.objects.all()
    serializer_class = SensorMapSerializer

class SensorMapDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor map instance.
    """
    queryset = SensorMap.objects.all()
    serializer_class = SensorMapSerializer


class SensorList(generics.ListCreateAPIView):
    """
    List all sensors, or create a new sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor instance.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ReadingList(generics.ListCreateAPIView):
    """
    List all readings, or create a new reading.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a reading instance.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class StatisticsList(generics.ListCreateAPIView):
    """
    List all statistics, or create a new statistic.
    """
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class StatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a statistic instance.
    """
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
