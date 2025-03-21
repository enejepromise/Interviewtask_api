from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

class InterviewSession(models.Model):
    """
    Representing the interview session with a title, description, and questions.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.TextField()
    scheduled_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_questions_list(self):
        """
        Returns the questions as a list, splitting by newline characters.
        """
        return [q.strip() for q in self.questions.splitlines() if q.strip()]

    class Meta:
        verbose_name = "Interview Session"
        verbose_name_plural = "Interview Sessions"
        ordering = ['-created_at'] 


class InterviewVideo(models.Model):
    title = models.CharField(max_length=255)  
    video = CloudinaryField('video', resource_type="video")  # Cloudinary storage
    video_url = models.URLField(blank=True, null=True)  
    duration = models.FloatField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.video and not self.video_url:  # Upload only if no Cloudinary URL
            try:
                upload_data = cloudinary.uploader.upload(self.video, resource_type="video")
                self.video_url = upload_data['secure_url']
                self.duration = upload_data.get('duration', 0)
            except cloudinary.exceptions.Error as e:
                print(f"Cloudinary upload failed: {e}")  # Log the error
        super().save(*args, **kwargs)

class Evaluation(models.Model):
    evaluator_name = models.CharField(max_length=255)
    user_id = models.IntegerField()  
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation by {self.evaluator_name} - Score: {self.score}"