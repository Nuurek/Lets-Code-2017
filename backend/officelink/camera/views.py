from rest_framework import viewsets, mixins

from .models import Room, Camera, Measurement
from .serializers import RoomSerializer, CameraSerializer, MeasurementSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_object(self):
        room = super(RoomViewSet, self).get_object()
        room.number_of_requests += 1
        room.save()
        return room
    
    def create(self, request, *args, **kwargs):
        room = super(RoomViewSet, self).create(request, *args, **kwargs)
        return room


class CameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
