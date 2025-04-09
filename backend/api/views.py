from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    data = {}

    try:
        data = json.loads(request.body)
    except:
        data = None
    
    print(f"Get url params: {request.GET}")
    print(data)
    data['params'] = dict(request.GET)
    return JsonResponse(f"Data from API: {data}", safe=False)
    