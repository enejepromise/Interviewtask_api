from django.contrib import admin
from .models import InterviewSession

@admin.register(InterviewSession)
class InterviewSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "scheduled_date", "created_at", "updated_at")  
    search_fields = ("title",) 
    list_filter = ("scheduled_date", "created_at", "updated_at")  
    ordering = ("-created_at",)
