from rest_framework.viewsets import ModelViewSet
from recommendation_circle.models import Recommendation
from recommendation_circle.serializers import RecommendationSerializer


class RecommendationViewSet(ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
