from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True, related_name="answer"
    )
