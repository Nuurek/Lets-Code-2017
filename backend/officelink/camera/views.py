from rest_framework import viewsets, mixins, response, generics, status

from .models import Room, Camera, Measurement
from .serializers import RoomSerializer, CameraSerializer, MeasurementSerializer


class RoomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, *args, **kwargs):
        room = self.get_object()
        room.number_of_requests += 1
        room.save()
        return super(RoomViewSet, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(RoomViewSet, self).create(request, *args, **kwargs)


class RoomHighestOccurrenceView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.order_by('-number_of_requests')[:3]


class CameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


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