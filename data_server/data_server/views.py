
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from actors.models import Deployment, Node, ConfigurationSequence, SensorMap, Sensor, Reading, Statistics
from data_server.serializers import DeploymentSerializer, NodeSerializer, ConfigSeqSerializer, SensorMapSerializer, SensorSerializer, ReadingSerializer, StatisticsSerializer
from data_server.permissions import IsOwnerOrReadOnly

# from rest_framework.authentication import SessionAuthentication as OriginalSessionAuthentication

# class SessionAuthentication(OriginalSessionAuthentication):
#     def enforce_csrf(self, request):
#         return

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'deployments': reverse('deployment-list', request=request, format=format),
        'nodes': reverse('node-list', request=request, format=format),
        'confseqs': reverse('confseq-list', request=request, format=format),
        'sensormaps': reverse('sensormap-list', request=request, format=format),
        'sensors': reverse('sensor-list', request=request, format=format),
        'readings': reverse('reading-list', request=request, format=format),
        'statistics': reverse('statistics-list', request=request, format=format)
    })

class DeploymentList(generics.ListCreateAPIView):
    """
    List all deployments, or create a new deployment.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                      # IsOwnerOrReadOnly)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class DeploymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a deployment instance.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                   IsOwnerOrReadOnly,)


class NodeList(generics.ListCreateAPIView):
    """
    List all nodes, or create a new node.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                   IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a node instance.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                   IsOwnerOrReadOnly,)


class ConfSeqList(generics.ListCreateAPIView):
    """
    List all configurationsequences, or create a new configurationsequence.
    """
    queryset = ConfigurationSequence.objects.all()
    serializer_class = ConfigSeqSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)    


class ConfSeqDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a configurationsequence instance.
    """
    queryset = ConfigurationSequence.objects.all()
    serializer_class = ConfigSeqSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SensorMapList(generics.ListCreateAPIView):
    """
    List all sensor maps, or create a new sensor map.
    """
    queryset = SensorMap.objects.all()
    serializer_class = SensorMapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SensorMapDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor map instance.
    """
    queryset = SensorMap.objects.all()
    serializer_class = SensorMapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SensorList(generics.ListCreateAPIView):
    """
    List all sensors, or create a new sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor instance.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ReadingList(generics.ListCreateAPIView):
    """
    List all readings, or create a new reading.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a reading instance.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatisticsList(generics.ListCreateAPIView):
    """
    List all statistics, or create a new statistic.
    """
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a statistic instance.
    """
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
