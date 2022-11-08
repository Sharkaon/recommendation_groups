from rest_framework.viewsets import ModelViewSet


class CircleViewSet(ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

