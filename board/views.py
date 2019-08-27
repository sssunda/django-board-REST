from django.shortcuts import render
from .models import Posting, Comment
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer,  UserSerializer
from django.contrib.auth.models import User

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
