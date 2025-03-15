from django.urls import path
from .views import (
    InterviewSessionListView,
    InterviewSessionDetailView,
    InterviewSessionCreateView
)

urlpatterns = [
    path("interviews/", InterviewSessionListView.as_view(), name="interview-list"),
    path("interviews/<int:pk>/", InterviewSessionDetailView.as_view(), name="interview-detail"),
    path("interviews/create/", InterviewSessionCreateView.as_view(), name="interview-create"),
]
