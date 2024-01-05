from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ScholarshipApp.models import Internationals,Locals
from ScholarshipApp.serializers import InternationalSerializer,LocalSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def internationalApi(request,id=0):
    if request.method=='GET':
        internationals = Internationals.objects.all()
        internationals_serializer=InternationalSerializer(internationals,many=True)
        return JsonResponse(internationals_serializer.data,safe=False)
    elif request.method=='POST':
        international_data=JSONParser().parse(request)
        internationals_serializer=InternationalSerializer(data=international_data)
        if internationals_serializer.is_valid():
            internationals_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        international_data=JSONParser().parse(request)
        international=Internationals.objects.get(InternationalId=international_data['InternationalId'])
        internationals_serializer=InternationalSerializer(international,data=international_data)
        if internationals_serializer.is_valid():
            internationals_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        international=Internationals.objects.get(InternationalId=id)
        international.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def localApi(request,id=0):
    if request.method=='GET':
        locals = Locals.objects.all()
        locals_serializer=LocalSerializer(locals,many=True)
        return JsonResponse(locals_serializer.data,safe=False)
    elif request.method=='POST':
        local_data=JSONParser().parse(request)
        locals_serializer=LocalSerializer(data=local_data)
        if locals_serializer.is_valid():
            locals_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        local_data=JSONParser().parse(request)
        local=Locals.objects.get(LocalId=local_data['LocalId'])
        locals_serializer=LocalSerializer(local,data=local_data)
        if locals_serializer.is_valid():
            locals_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        local=Locals.objects.get(LocalId=id)
        local.delete()
        return JsonResponse("Deleted Successfully",safe=False)

