from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.request.query_params.get('room')
        queryset = Message.objects.all().order_by('created_at')
        if room_id:
            queryset = queryset.filter(room_id=room_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)