"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from board import views

router = routers.DefaultRouter()
router.register(r'postings', views.PostingViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/postings/<int:pk>/', views.posting_detail),
    path('api/postings/<int:pk>/comments/', views.posting_comments),
    path('api/', include(router.urls)),    
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('board/', views.BoardView.as_view()),
]
