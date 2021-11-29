from django.contrib.auth import get_user_model
from django.db import models

from .poll import Poll

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='votes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
