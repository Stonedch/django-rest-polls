from django.db import models

from .question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
