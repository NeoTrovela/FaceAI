from django.db import models
# additions
from django.contrib.auth.models import User

# Create your models here.
class Pict(models.Model): # Notes model
    title = models.CharField(max_length=100) # added title
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # automatically populate when new instance of note is created
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") # who created note
    # foreign key -> lends user with data that belongs to the user
    # on_delete -> deletes notes with user is deleted
    # related_name -> what field name to put on user to reference all notes

    def __str__(self):
        return self.title
