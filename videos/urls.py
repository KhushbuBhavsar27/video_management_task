
from django.urls import path
from . import views
from .views import VideoUpload, VideoSearch, VideoUpdate, VideoDelete

urlpatterns = [
    path('upload/', VideoUpload.as_view(), name='video-upload'),
    path('search/', VideoSearch.as_view(), name='video-search'),
    path('update/<int:pk>/', VideoUpdate.as_view(), name='video-update'),
    path('delete/<int:pk>/', VideoDelete.as_view(), name='video-delete'),
    path('', views.video_list, name='video-list'),
]
