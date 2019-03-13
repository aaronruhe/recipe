from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test if creating a new user with an email is successful"""

    def test_create_user_with_email_successful(self):
        email = 'test@kpndev.com'
        password = 'Testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, '12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalied_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(
                ValueError):  # anything that we run in here should raise the value error else test will fail
            get_user_model().objects.create_user(None, '12345')

    def test_create_new_super_user(self):
        """Test create a new super user"""

        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
