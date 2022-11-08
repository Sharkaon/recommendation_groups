from django.urls import include
from rest_framework import routers
from recommendation_circle.views import RecommendationViewSet, CircleViewSet, EditionViewSet

router = routers.DefaultRouter()
router.register('recommendation', RecommendationViewSet, basename='Recommendation')
router.register('circle', CircleViewSet, basename='Circle')
router.register('edition', EditionViewSet, basename='Edition')
