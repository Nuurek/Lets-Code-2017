from rest_framework import viewsets

from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_object(self):
        room = super(RoomViewSet, self).get_object()
        room.number_of_requests += 1
        room.save()
        return room
