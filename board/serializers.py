from .models import Posting,Comment
from rest_framework import serializers, pagination
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = User
        fields = ('url','username')
        
class PostingSerializer(serializers.HyperlinkedModelSerializer):
    name = UserSerializer()
    class Meta:
        model = Posting
        fields = ('title','name', 'url','create_date')

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('posting', 'name', 'text')

class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
    name = UserSerializer()
    class Meta:
        model=Posting
        fields = ('title', 'name', 'text', 'create_date', 'modified_date')

class CustomPagination(pagination.PageNumberPagination):
    
    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })