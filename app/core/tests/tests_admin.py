from django.test import TestCase, Client  # Client allows test requests
from django.contrib.auth import get_user_model
from django.urls import reverse  # generate urls


# admin page unit tests

class AdminSiteTests(TestCase):

    def setUp(self):
        """Setup tasks run before tests are run"""
        """
        1. Create test client, 
        2. Add a new user to test, 
        3. User logs into our client, 
        4. Create regular user that is not authenticated
        """

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='testz@test.com',
            password='1234'
        )

        """So what this does is it uses the client helper function that allows you to log a user in with the Django
        authentication. And this really helps make our tests a lot easier to write because it means we don't have to 
        manually log the user in which Candace uses helper function our list to the official documentation of the test
        """
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@tests.com',
            password='1234',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user pages"""
        # reverse changes this url everywhere in our tests / urls of Django admin are in Django docs
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)  # perform http get on the url

        self.assertContains(response, self.user.name)  # assertContains checks for 200 AND can check model values
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id]) # admin/core/user/1 (1 = id, args is id here)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)