import unittest
from django.urls import reverse
from django.test import Client
from .models import DaysOfTheWeek
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_daysoftheweek(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["day"] = "day"
    defaults.update(**kwargs)
    return DaysOfTheWeek.objects.create(**defaults)


class DaysOfTheWeekViewTest(unittest.TestCase):
    '''
    Tests for DaysOfTheWeek
    '''
    def setUp(self):
        self.client = Client()

    def test_list_daysoftheweek(self):
        url = reverse('foodifyapp_daysoftheweek_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_daysoftheweek(self):
        url = reverse('foodifyapp_daysoftheweek_create')
        data = {
            "id": "id",
            "day": "day",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_daysoftheweek(self):
        daysoftheweek = create_daysoftheweek()
        url = reverse('foodifyapp_daysoftheweek_detail', args=[daysoftheweek.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_daysoftheweek(self):
        daysoftheweek = create_daysoftheweek()
        data = {
            "id": "id",
            "day": "day",
        }
        url = reverse('foodifyapp_daysoftheweek_update', args=[daysoftheweek.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
