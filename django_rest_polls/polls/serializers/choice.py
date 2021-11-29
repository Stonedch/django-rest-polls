from rest_framework import serializers

from polls.models import Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'content')
        read_only_fields = ('id', )
