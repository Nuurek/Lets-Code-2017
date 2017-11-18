from rest_framework import serializers

from .models import Room, Camera


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('name', 'camera', 'maximum_capacity')


class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera
        fields = ('serial_number',)
