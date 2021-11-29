from rest_framework.serializers import ModelSerializer

from polls.models import Poll


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'created_at', 'end_date')
        read_only_fields = ('id', 'created_at')
