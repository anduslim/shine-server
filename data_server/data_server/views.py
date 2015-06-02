from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from actors.models import Deployment, Node
from data_server.serializers import DeploymentSerializer, NodeSerializer, ConfigSeqSerializer, SensorMapSerializer, SensorSerializer, ReadingSerializer, StatisticsSerializer



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
        deployement = Deployment.objects.get(pk=pk)
    except Deployment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeploymentSerializer(deployement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeploymentSerializer(deployement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        deployement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nodes to be viewed or edited.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer