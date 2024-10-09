from django.shortcuts import render , get_object_or_404 , redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import vd_Serializer
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})

class VideoUpload(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = vd_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class VideoSearch(APIView):
    def get(self, request):
        title = request.GET.get('title', None)
        if title:
            try:
                video = Video.objects.get(vd_name=title)
                serializer = vd_Serializer(video)
                return Response(serializer.data)
            except Video.DoesNotExist:
                return Response({"error": "Video not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Title query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        
class VideoUpdate(APIView):
    def get(self, request, pk):
        video = get_object_or_404(Video, pk=pk)
        serializer = vd_Serializer(video)
        return render(request, 'videos/vd_update.html', {'serializer': serializer, 'video': video})

    def post(self, request, pk):
        video = get_object_or_404(Video, pk=pk)
        serializer = vd_Serializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('video-list')  # Redirect to the video list after successful update
        return render(request, 'videos/vd_update.html', {'video': video,'serializer': serializer})

          
class VideoDelete(APIView):
    def delete(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            video.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=status.HTTP_404_NOT_FOUND)






