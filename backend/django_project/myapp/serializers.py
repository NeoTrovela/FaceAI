from django.contrib.auth.models import User
from rest_framework import serializers

# serializers -> with API, taken python object and converts to JSON data in order to commute with other apps, vice versa
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # model we want to serialize, user model (built in Django represents a user)
        fields = ["id", 'username', 'password'] # field we want to serialize when we are accepting and returning new user
        extra_kwargs = {'password' : {'write_only': True}} # tells django we want to accept password, but don't want to return password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # implement method called when creating new version of user

        return user
    
class NoteSerializer(serializers.ModelSerializer): # add serializer for Notes model
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {'author' : {'read_only':True}} # only read who author is