from datetime import datetime, timedelta
from django.urls import reverse
from users.tests import BaseTest
from .models import Shift
import json


class ShiftTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.shift = Shift.objects.create(
            user=self.user, hour=self.hour, date=self.date)


class ShiftModelTest(ShiftTest):
    def setUp(self):
        super().setUp()

    def test_hour(self):
        self.assertEqual(self.shift.hour, self.hour)
        meta_data = self.shift._meta.get_field('hour')
        self.assertEqual(meta_data.default, 0)
        self.assertTrue(not meta_data.null)

    def test_date(self):
        meta_data = self.shift._meta.get_field('date')
        self.assertTrue(not meta_data.null)

    def test_user(self):
        self.assertEqual(self.shift.user.id, self.user.id)


class ShiftViewTest(ShiftTest):
    def setUp(self):
        super().setUp()
        self.get_token()

    def get_token(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        response_data = json.loads(response.content)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(
            response_data.get("token"))}

    def test_create(self):
        response = self.client.post(reverse('shift-list'), {
            'user_id': self.user.id,
            'date': self.date,
            'hour': 1
        }, **self.header)
        self.assertEqual(response.status_code, 400)

    def test_get(self):
        response = self.client.get(reverse('shift-list'), **self.header)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 1)

    def test_retrieve(self):
        response = self.client.get(
            reverse('shift-detail', kwargs={'pk': self.shift.id}), **self.header)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('id'), self.shift.id)

    def test_partial_update(self):
        response = self.client.patch(
            reverse('shift-detail', kwargs={'pk': self.shift.id}), {
                'date': self.date2
            }, **self.header, content_type='application/json')
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('date'), self.date2)

    def test_delete(self):
        response = self.client.delete(reverse('shift-detail', kwargs={
            'pk': self.shift.id
        }), **self.header)
        self.assertEqual(response.status_code, 204)
