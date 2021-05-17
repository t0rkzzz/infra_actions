from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class StaticPagesURLTests(TestCase):
    @classmethod
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = self.guest_client.get(reverse('infra_app:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response = self.guest_client.get(reverse('infra_app:second_page'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_shows_correct_context(self):
        """Проверка контекста страниц."""
        response = self.guest_client.get(reverse('infra_app:index'))
        self.assertContains(response, 'У меня получилось!')
        response = self.guest_client.get(reverse('infra_app:second_page'))
        self.assertContains(response, 'А это вторая страница!')
