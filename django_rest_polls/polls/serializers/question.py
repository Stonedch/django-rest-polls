from rest_framework import serializers

from polls.models import Poll, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'poll', 'content', 'type')
        read_only_fields = ('id', )
        extra_kwargs = {
            'poll': {'write_only': True}
        }
