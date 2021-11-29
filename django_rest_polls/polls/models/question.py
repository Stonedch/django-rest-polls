from django.db import models

from .poll import Poll


class Question(models.Model):
    class Type:
        TEXT = 'text'
        SINGLE_CHOICE = 'singlechoice'
        MULTIPLE_CHOICE = 'multiplechoice'

        CHOICES = (
            (TEXT, 'Text answer'),
            (SINGLE_CHOICE, 'Single choice answer'),
            (MULTIPLE_CHOICE, 'Multiple choice answer'),
        )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField(max_length=300)
    type = models.CharField(max_length=14, choices=Type.CHOICES, default=Type.TEXT)
