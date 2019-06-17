from .models import Posting,Comment
from rest_framework import serializers

class PostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('name', 'title', 'text')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('posting', 'name', 'text')

