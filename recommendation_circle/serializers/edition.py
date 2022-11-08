from rest_framework import serializers
from recommendation_circle.models import Edition


class EditionSerializer(serializers.ModelSerializer):
    recommendations = serializers.StringRelatedField(many=True)

    class Meta:
        model = Edition
        fields = ['id', 'order', 'circle', 'number', 'recommendations']
