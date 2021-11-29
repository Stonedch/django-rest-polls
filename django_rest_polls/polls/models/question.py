from django.db import models

from .poll import Poll


class Question(models.Model):
    class Type:
        TEXT = 'text'
        SINGLE_CHOISE = 'singlechoise'
        MULTIPLE_CHOISE = 'multiplechoise'

        CHOICES = (
            (TEXT, 'Text answer'),
            (SINGLE_CHOISE, 'Single choise answer'),
            (MULTIPLE_CHOISE, 'Multiple choise answer'),
        )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField(max_length=300)
    type = models.CharField(max_length=14, choices=Type.CHOICES, default=Type.TEXT)
