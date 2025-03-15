from django.db import models

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