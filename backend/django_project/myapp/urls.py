from django.urls import path
from . import views

urlpatterns = [
    path("pics/", views.PictListCreate.as_view(), name="pic-list"), # viewing / creating note
    path("pics/delete/<int:pk>/", views.PictDelete.as_view(), name="delete-pict"), # deleting note
    # <int:pk> means primary key
]