from django.contrib.auth.models import User
from django.db import models

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    text = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField(Answer, blank=True, related_name='question')

