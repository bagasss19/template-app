from rest_framework import serializers
from .models import Post
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','media', 'content')