from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test1234'
        )

        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('test1234'))