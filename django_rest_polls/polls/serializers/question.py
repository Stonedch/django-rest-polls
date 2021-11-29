from rest_framework import serializers

from .choice import ChoiceSerializer
from polls.models import Poll, Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Question.Type.CHOICES, default=Question.Type.TEXT)
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'content', 'type', 'choices')
        read_only_fields = ('id', )
        extra_kwargs = {
            'poll': {'write_only': True}
        }

    def create_choices(self, question, choices):
        Choice.objects.bulk_create([
            Choice(question=question, **choice) for choice in choices
        ])

    def create(self, validated_data):
        choices = validated_data.pop('choices', [])
        print(f'### TEST: {choices}')
        question = Question.objects.create(**validated_data)
        self.create_choices(question, choices)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices', [])
        print(f'### TEST: {choices}')
        instance.choices.all().delete()
        self.create_choices(instance, choices)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
