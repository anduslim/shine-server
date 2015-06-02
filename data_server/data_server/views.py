
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from actors.models import Deployment, Node, ConfigurationSequence
from data_server.serializers import DeploymentSerializer, NodeSerializer, ConfigSeqSerializer, SensorMapSerializer, SensorSerializer, ReadingSerializer, StatisticsSerializer

class DeploymentList(APIView):
    """
    List all deployments, or create a new deployment.
    """
    def get(self, request, format=None):
        deployments = Deployment.objects.all()
        serializer = DeploymentSerializer(deployments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeploymentDetail(APIView):
    """
    Retrieve, update or delete a deployment instance.
    """
    def get_object(self, pk):
        try:
            return Deployment.objects.get(pk=pk)
        except Deployment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deployment = self.get_object(pk)
        serializer = DeploymentSerializer(deployment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deployment = self.get_object(pk)
        serializer = DeploymentSerializer(deployment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deployment = self.get_object(pk)
        deployment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

