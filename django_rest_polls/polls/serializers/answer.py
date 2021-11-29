from rest_framework import serializers

from .choice import ChoiceSerializer
from .question import QuestionSerializer
from polls.models import Poll, Question, Choice, Answer
from polls.fields import ObjectIDField


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    choice_id = ObjectIDField(queryset=Choice.objects.all(), write_only=True)

    question = QuestionSerializer(read_only=True)
    question_id = ObjectIDField(queryset=Question.objects.all(), write_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'question_id', 'question', 'choice_id', 'choice', 'value')
        read_only_fields = ('id', )
