from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .models import Record
import json

def index(request):
    return render(request, "records/index.html")

def csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def get_records(request):
    if request.method == 'GET':
        data = list(Record.objects.values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        record = Record.objects.create(name=body['name'], email=body['email'])
        return JsonResponse({'id': record.id, 'name': record.name, 'email': record.email}, status=201)

@csrf_exempt
def record_detail(request, id):
    try:
        record = Record.objects.get(id=id)
    except Record.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

    if request.method == 'PUT':
        body = json.loads(request.body)
        record.name = body['name']
        record.email = body['email']
        record.save()
        return JsonResponse({'id': record.id, 'name': record.name, 'email': record.email})
    elif request.method == 'DELETE':
        record.delete()
        return JsonResponse({'message': 'Record deleted'}, status=204)
