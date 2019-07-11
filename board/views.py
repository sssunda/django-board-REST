from django.shortcuts import render
from .models import Posting, Comment
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer, PostingDetailSerializer, UserSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView 
from django.contrib.auth.models import User

# Create your views here.
class BoardView(TemplateView): 
    template_name = 'board/list.html'

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def posting_detail(request, pk):
    try:
        posting = Posting.objects.get(pk=pk)
    except Posting.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = PostingDetailSerializer(posting, context={'request': request})
        return JsonResponse(serializer.data)

@csrf_exempt
def posting_comments(request, pk):
    try:
        comments = Posting.objects.get(pk=pk).comment_set.all()
    
    except Posting.DoesNotExist:
        return HttpResponse(status=404)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)
    
    if len(comments) ==0 :
        return HttpResponse(status=404)

    if request.method =='GET':
        serializer = CommentSerializer(comments, context={'request': request}, many= True)
        return JsonResponse(serializer.data, safe = False)