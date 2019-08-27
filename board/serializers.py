from .models import Posting,Comment
from rest_framework import serializers, pagination
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True) 
    
    class Meta:
        model = Comment
        fields = ('posting', 'user', 'text', 'pk')
        
class PostingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    comment = CommentSerializer(many=True, read_only= True)

    class Meta:
        model = Posting 
        fields = ('title', 'user','text','modified_date','pk', 'comment')