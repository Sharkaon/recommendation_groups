from django.urls import include
from rest_framework import routers
from recommendation_circle.views import RecommendationViewSet, CircleViewSet

router = routers.DefaultRouter()
router.register('recommendation', RecommendationViewSet, basename='Recommendation')
router.register('circle', CircleViewSet, basename='Circle')
