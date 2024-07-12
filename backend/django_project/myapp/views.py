from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


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


# views for creating/deleting Note
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # cant call root if authenticated and passes valid jwt token
    # list all notes created by user or created new note

    def get_queryset(self):
        user = self.request.user # gets user that is authenticated and interacting with root
        return Note.objects.filter(author=user) # gets all Notes written by user
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) # makes new version of note, adds author onto note
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # gets user that is authenticated and interacting with root
        return Note.objects.filter(author=user) # gets all Notes written by user



# functions to allow creation of new users
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer # kind of data needed to make a new user
    permission_classes = [AllowAny] # allows anyone to be able to make a new user