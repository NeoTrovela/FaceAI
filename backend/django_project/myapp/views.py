from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def api_data(request):
    data = {
        "key": "value",
        "message": "Django"
    }

    return JsonResponse(data)

def http_view(request):

    return HttpResponse("<h1>Welcome to NameOfWebsite</h1>")