from django.test import TestCase
from django.urls import reverse
from users.models import Account
import json
from datetime import datetime, timedelta


class BaseTest(TestCase):
    def setUp(self):
        # set common values
        self.username = 'user'
        self.password = 'password'
        self.hour = 0
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.date2 = (datetime.today() + timedelta(days = 1)).strftime('%Y-%m-%d')

        # set user
        self.user = Account.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.save()


class AccountTest(BaseTest):
    def setUp(self):
        super().setUp()


class AccountModelTest(AccountTest):
    def setUp(self):
        super().setUp()

    def test_username(self):
        self.assertEqual(self.user.username, self.username)
        meta_data = self.user._meta.get_field('username')
        self.assertEqual(meta_data.max_length, 50)
        self.assertTrue(meta_data.unique)


class AccountViewTest(AccountTest):
    def setUp(self):
        super().setUp()

    def test_register(self):
        response = self.client.post(reverse('register'), {
            "username": "user2",
            "password": "password2"
        }, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post(reverse('login'), {
            "username": "user",
            "password": "password"
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue("token" in response_data.keys())
