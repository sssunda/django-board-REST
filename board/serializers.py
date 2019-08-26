from .models import Posting,Comment
from rest_framework import serializers, pagination
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        
class PostingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Posting 
        fields = ('title', 'user','text','modified_date','pk')
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.text = validated_data['text']
        instance.save()

        return instance

    def destroy(self, instance):
        instance.delete()

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True) 
    class Meta:
        model = Comment
        fields = ('posting', 'user', 'text')