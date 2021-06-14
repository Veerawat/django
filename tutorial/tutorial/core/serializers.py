from rest_framework import serializers
from core.models import Subscriber, Profile



class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=False)
    def create(self, validated_data):
        return Subscriber.objects.create(**validated_data)


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    nick_name = serializers.CharField(max_length=300)
    email = serializers.CharField(max_length=300)
    tel = serializers.CharField(max_length=300)
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
