from rest_framework import serializers

from .answer import AnswerSerializer
from .poll import PollSerializer
from polls.models import Poll, Choice, Vote, Answer
from polls.fields import ObjectIDField


class VoteSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    poll = PollSerializer(read_only=True)
    poll_id = ObjectIDField(
        queryset=Poll.active_objects.all(),
        write_only=True
    )

    class Meta:
        model = Vote
        fields = ('id', 'poll_id', 'poll', 'user', 'created_at', 'answers')
        read_only_fields = ('id', 'user', 'created_at')

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        instance = Vote.objects.create(**validated_data)
        Answer.objects.bulk_create([
            Answer(vote=instance, **answer) for answer in answers
        ])
        return instance
