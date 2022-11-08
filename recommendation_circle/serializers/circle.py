from rest_framework import serializers
from recommendation_circle.models import Circle
from recommendation_circle.serializers import EditionSerializer


class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'


class CircleLastEditionSerializer(serializers.ModelSerializer):
    last_edition_dict = serializers.SerializerMethodField()

    @staticmethod
    def get_last_edition_dict(circle):
        last_edition_number = circle.last_edition
        last_edition_obj = circle.editions.all()[last_edition_number - 1]
        serialized = EditionSerializer(last_edition_obj)
        return serialized.data

    class Meta:
        model = Circle
        fields = ['id', 'name', 'participants', 'last_edition_dict']
