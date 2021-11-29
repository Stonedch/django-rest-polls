from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from polls.urls import router as polls_router

router = DefaultRouter(trailing_slash=True)

router.registry.extend(polls_router.registry)

urlpatterns = [
    path('api/', include([
        path('', include(router.urls), name='router'),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]), name='api'),
]
