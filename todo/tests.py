from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(description='Test Task', user=self.user)
        self.login = self.client.login(username='testuser', password='12345')

    def test_create_task(self):
        response = self.client.post(reverse('task_create'), {'description': 'New Task'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(description='New Task').exists())
        self.assertEqual(Task.objects.filter(description='New Task').first().user, self.user)

    def test_update_task(self):
        response = self.client.post(reverse('task_update', args=[self.task.id]), {'description': 'Updated Task'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.filter(description='Updated Task').first().user, self.user)

    def test_delete_task(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(description='Test Task').exists())

