from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from vlog.models import Video
from vlog.serializers import VideoSerializer



@csrf_exempt
def vlog_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        vlogs = Video.objects.all()
        serializer = VideoSerializer(vlogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def vlog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        vlog = Video.objects.get(id=pk)
    except Video.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoSerializer(vlog)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(vlog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vlog.delete()
        return HttpResponse(status=204)