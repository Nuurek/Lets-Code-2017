from rest_framework import serializers

from .models import Room, Camera, Measurement


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'camera', 'current_capacity', 'maximum_capacity')


class RoomPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('name', 'camera', 'maximum_capacity')


class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera
        fields = ('serial_number',)


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('value', 'timestamp', 'camera')
