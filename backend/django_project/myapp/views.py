from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_data(request):
    data = {
        "key": "value",
        "message": "Django"
    }

    return JsonResponse(data)