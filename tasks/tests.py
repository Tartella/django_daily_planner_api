from rest_framework.test import APITestCase
from django.urls import reverse

class TaskAPITest(APITestCase):
    def test_create_and_get_tasks(self):
        url = reverse('task-list')
        data = {'title': 'Test Task', 'description': 'From test', 'is_completed': False}
        self.client.post(url, data, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)
