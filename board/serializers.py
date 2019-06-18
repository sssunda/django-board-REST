from .models import Posting,Comment
from rest_framework import serializers

class PostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('create_date', 'url', 'name', 'title')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('posting', 'name', 'text')

class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Posting
        fields = ('name', 'title', 'text', 'create_date', 'modified_date')