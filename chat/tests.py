from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Room, Message


class ChatModelTests(TestCase):
    def test_create_room(self):
        room = Room.objects.create(name='General')
        self.assertEqual(str(room), 'General')

    def test_create_message(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test1234'
        )
        room = Room.objects.create(name='General')
        message = Message.objects.create(
            room=room,
            user=user,
            content='Hello'
        )
        self.assertEqual(message.content, 'Hello')
        self.assertEqual(message.room.name, 'General')