from rest_framework import serializers
from .models import InterviewSession, InterviewVideo


class InterviewSessionSerializer(serializers.ModelSerializer):
    """Serializer for the InterviewSession model"""

    class Meta:
        model = InterviewSession
        fields = ['id', 'title', 'description', 'questions']


class InterviewVideoSerializer(serializers.ModelSerializer):
    """Serializer for the InterviewVideo model"""

    class Meta:
        model = InterviewVideo
        fields = '__all__' 

class InterviewVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewVideo
        fields = ['id', 'title', 'video_url']
