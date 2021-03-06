from rest_framework.routers import DefaultRouter

from polls.viewsets import PollViewSet, QuestionViewSet, VoteViewSet

router = DefaultRouter(trailing_slash=True)

router.register('polls/?', PollViewSet, 'polls')
router.register('questions/?', QuestionViewSet, 'questions')
router.register('votes/?', VoteViewSet)
