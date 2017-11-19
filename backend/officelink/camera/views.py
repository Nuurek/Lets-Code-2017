from rest_framework import viewsets, mixins, response, generics, views, status
from django.shortcuts import get_object_or_404

from .models import Room, Camera, Measurement
from .serializers import RoomSerializer, CameraSerializer, MeasurementSerializer, RoomPostSerializer


class RoomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        return super(RoomViewSet, self).create(request, *args, **kwargs)


class CameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        response = super(MeasurementCreateView, self).create(request, *args, **kwargs)
        room = Room.objects.get(camera__serial_number=response.data['camera'])
        room.current_capacity = response.data['value']
        room.save()
        return response

    def post(self, request, format=None):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)