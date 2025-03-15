from rest_framework import serializers
from .models import InterviewSession  # Correct model name

class InterviewSessionSerializer(serializers.ModelSerializer):  # Correct serializer name
    """Serialize the InterviewSession model"""

    class Meta:
        model = InterviewSession  # Correct model name
        fields = ["id", "title", "description", "questions", "created_at", "updated_at"] #Correct field