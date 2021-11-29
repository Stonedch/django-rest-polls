from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from polls.models import Vote
from polls.serializers import VoteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    http_method_names = ('get', 'post')
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)

        return super().perform_create(serializer)
