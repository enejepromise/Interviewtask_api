from django.urls import path
from .views import (
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
    path("upload/", UploadVideoView.as_view(), name="upload-video"),
    path("videos/", ListVideosView.as_view(), name="list-videos"),
]
