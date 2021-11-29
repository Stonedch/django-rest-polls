from rest_framework.routers import DefaultRouter

from polls.viewsets import PollViewSet

router = DefaultRouter(trailing_slash=True)

router.register('polls/?', PollViewSet, 'polls')
