from rest_framework import serializers
from recommendation_circle.models import Circle
from recommendation_circle.serializers import EditionSerializer


class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'


