
from rest_framework import serializers
from .models import Video

class vd_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'vd_name', 'description', 'vd_file', 'upload_time']
