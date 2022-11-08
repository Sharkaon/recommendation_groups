from rest_framework.viewsets import ModelViewSet
from recommendation_circle.models import Edition
from recommendation_circle.serializers import EditionSerializer


class EditionViewSet(ModelViewSet):
    serializer_class = EditionSerializer
    queryset = Edition.objects.all()
