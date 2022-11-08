from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from recommendation_circle.models import Circle, Edition
from recommendation_circle.serializers import CircleSerializer, CircleLastEditionSerializer


class CircleViewSet(ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

    @action(detail=False, methods=['post'])
    def start_new_edition(self, request):
        if request.data == {}:
            raise ParseError()

        circle_id = request.data['id']

        if circle_id is None:
            raise ParseError()

        circle_of_new_edition = get_object_or_404(Circle, pk=circle_id)
        last_edition = circle_of_new_edition.last_edition or 0
        new_edition = Edition(
            number=last_edition + 1,
            circle_id=circle_id,
        )
        new_edition.save()

        res = Response({'id': new_edition.id})
        res.status_code = status.HTTP_201_CREATED

        return res

    def retrieve(self, request, pk=None, *args, **kwargs):
        circle = self.queryset.get(pk=pk)

        if circle is None:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        serializer = CircleLastEditionSerializer(circle)

        if not serializer.is_valid:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
