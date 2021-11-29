from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from polls.models import Poll
from polls.serializers import PollSerializer
from polls.permissions import ReadOnly


class PollViewSet(ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [IsAdminUser|ReadOnly]

    def list(self, request: Request, *args, **kwargs):
        if request.user.is_staff:
            queryset = Poll.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        queryset = Poll.active_objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
