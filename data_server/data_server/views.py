
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from actors.models import Deployment, Node, ConfigurationSequence
from data_server.serializers import DeploymentSerializer, NodeSerializer, ConfigSeqSerializer, SensorMapSerializer, SensorSerializer, ReadingSerializer, StatisticsSerializer

class DeploymentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all deployments, or create a new deployment.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DeploymentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a deployment instance.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def deployment_list(request, format=None):
    """
    List all deployments, or create a new deployment.
    """
    if request.method == 'GET':
        deployments = Deployment.objects.all()
        serializer = DeploymentSerializer(deployments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def deployment_detail(request, pk, format=None):
    """
    Retrieve, update or delete a deployment instance.
    """
    try:
        deployment = Deployment.objects.get(pk=pk)
    except Deployment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeploymentSerializer(deployment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeploymentSerializer(deployment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        deployment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def node_list(request, format=None):
    """
    List all nodes, or create a new node.
    """
    if request.method == 'GET':
        nodes = Node.objects.all()
        serializer = NodeSerializer(nodes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def node_detail(request, pk, format=None):
    """
    Retrieve, update or delete a node instance.
    """
    try:
        node = Node.objects.get(pk=pk)
    except Node.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NodeSerializer(node)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NodeSerializer(node, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        node.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def confseq_list(request, format=None):
    """
    List all confseqs, or create a new confseq.
    """
    if request.method == 'GET':
        confseqs = ConfigurationSequence.objects.all()
        serializer = ConfigSeqSerializer(confseqs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConfigSeqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def confseq_detail(request, pk, format=None):
    """
    Retrieve, update or delete a confseq instance.
    """
    try:
        confseq = ConfigurationSequence.objects.get(pk=pk)
    except ConfigurationSequence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConfigSeqSerializer(confseq)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConfigSeqSerializer(confseq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        confseq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

