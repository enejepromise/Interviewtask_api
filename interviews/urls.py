from django.urls import path
from .views import (
    EvaluationCreateAPIView,  # Make sure this view exists in views.py
    EvaluationListView,       # Make sure this view exists in views.py
    UploadVideoView,
    ListVideosView,
    InterviewSessionListView,
    InterviewSessionDetailView,
    InterviewSessionCreateView
)

urlpatterns = [
    path("interviews/", InterviewSessionListView.as_view(), name="interview-list"),
    path("interviews/<int:pk>/", InterviewSessionDetailView.as_view(), name="interview-detail"),
    path("interviews/create/", InterviewSessionCreateView.as_view(), name="interview-create"),
    path("videos/upload/", UploadVideoView.as_view(), name="upload-video"),
    path("videos/", ListVideosView.as_view(), name="list-videos"),
    path('evaluations/', EvaluationListView.as_view(), name='evaluation-list'),  # List all evaluations
    path('evaluations/create/', EvaluationCreateAPIView.as_view(), name='evaluation-create'),  # Create a new evaluation
]
