import datetime

from django.core.exceptions import ValidationError
from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        today = datetime.datetime.now()
        return super().get_queryset().filter(end_date__gte=today)


class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return f'{self.title}'
