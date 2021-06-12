from rest_framework import serializers
from core.models import Subscriber



class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=False)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Subscriber.objects.create(**validated_data)
