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
]
