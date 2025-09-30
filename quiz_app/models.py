from django.db import models


class Question(models.Model):
    question_title = models.CharField(max_length=256)
    question_options = models.JSONField()
    answer = models.CharField(max_length=256)

class Quiz(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_now=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    questions = models.OneToOneField(Question, related_name='questions', on_delete=models.CASCADE)