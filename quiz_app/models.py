from django.db import models
    
class Quiz(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)

class Question(models.Model):
    question_title = models.CharField(max_length=256)
    question_options = models.JSONField()
    answer = models.CharField(max_length=256)    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE, null=True)