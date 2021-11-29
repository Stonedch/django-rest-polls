from django.db import models

from .question import Question
from .vote import Vote
from .choice import Choice


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='answers', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE)
    value = models.TextField(max_length=300, blank=True, null=True)
