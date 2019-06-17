from django.shortcuts import render
from .models import Posting, Comment
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer

# Create your views here.
class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer