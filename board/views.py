from django.shortcuts import render
from .models import Posting, Comment
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer,  UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

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

def posting_comments(request, pk):
    try :
        comments = Posting.objects.get(pk=pk).comment.all()

    except Posting.DoesNotExist:
        return HttpResponse(status=404)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)
    
    if len(comments) == 0 :
        return HttpResponse(status=404)

    if request.method =='GET':
        serializer = CommentSerializer(comments, context={'request': request}, many= True)
        return JsonResponse(serializer.data, safe = False)
