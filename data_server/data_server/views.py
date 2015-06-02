from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from actors.models import Deployment
from data_server.serializers import DeploymentSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def deployment_list(request):
    """
    List all code deployments, or create a new deployment.
    """
    if request.method == 'GET':
        deployments = Deployment.objects.all()
        serializer = DeploymentSerializer(deployments, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeploymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def deployment_detail(request, pk):
    """
    Retrieve, update or delete a code deployment.
    """
    try:
        deployment = Deployment.objects.get(pk=pk)
    except Deployment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeploymentSerializer(deployment)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(deployment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        deployment.delete()
        return HttpResponse(status=204)