from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import InterviewSession
from .serializers import InterviewSessionSerializer

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
