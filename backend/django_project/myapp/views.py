from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

# views function -> takes web request(JSON, HTTP, etc.), returns web response (JsonResponse, HttpResponse, etc)
# renders HTML/CSS/JS
# understand that frontend communicated to backend w/ requests, in which backend gives response
# need JWT (Json Web Token) so user can interact with backend. JWT is token that shows users permissions in website

def api_data(request):
    data = {
        "key": "value",
        "message": "Django"
    }

    return JsonResponse(data)

def http_view(request): 

    return HttpResponse("<h1>Welcome to NameOfWebsite</h1>")