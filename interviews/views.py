from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import cloudinary.uploader
from .models import Evaluation
from .serializers import EvaluationSerializer
from .models import InterviewSession, InterviewVideo
from .serializers import InterviewSessionSerializer, InterviewVideoSerializer, InterviewVideoListSerializer


class InterviewSessionPagination(PageNumberPagination):
    """
    Custom pagination class for InterviewSession objects
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class InterviewSessionListView(generics.ListAPIView):
    """
    API endpoint to list all interview sessions with pagination.
    """
    queryset = InterviewSession.objects.all().order_by('-created_at')
    serializer_class = InterviewSessionSerializer
    pagination_class = InterviewSessionPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InterviewSessionDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve details of a specific interview session by ID.
    """
    queryset = InterviewSession.objects.all()
    serializer_class = InterviewSessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InterviewSessionCreateView(generics.CreateAPIView):
    """
    API view for creating new interview sessions.
    """
    queryset = InterviewSession.objects.all()
    serializer_class = InterviewSessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UploadVideoView(generics.CreateAPIView):
    queryset = InterviewVideo.objects.all()
    serializer_class = InterviewVideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListVideosView(generics.ListAPIView):
    """
    API endpoint to list all interview videos.
    """
    queryset = InterviewVideo.objects.all()
    serializer_class = InterviewVideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from rest_framework import generics
from .models import Evaluation
from .serializers import EvaluationSerializer

class EvaluationListView(generics.ListAPIView): #Add this class
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class EvaluationCreateAPIView(generics.CreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer