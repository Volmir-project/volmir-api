from django.contrib.auth.hashers import make_password

import json
from django.test import TestCase, Client
from api.models import User, Post, Task


class TestSignupCreation(TestCase):
    def setUp(self):
        self.client = Client()

    def test_successful_user_creation(self):
        signup_data = {
            "email": "newuser@example.com",
            "firstName": "John",
            "lastName": "Doe",
            "username": "johndoe123",
            "password1": "securepassword123",
            "password2": "securepassword123"
        }

        response = self.client.post(
            '/auth/signup/',
            data=json.dumps(signup_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertIn('token', response_data)
        self.assertEqual(response_data['message'], 'User created successfully')

        user_exists = User.objects.filter(email='newuser@example.com').exists()
        self.assertTrue(user_exists)


class TestLoginAuthentication(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(
            email='test@example.com',
            password=make_password('testpassword123')
        )

    def test_successful_authentication(self):
        login_data = {
            'email': 'test@example.com',
            'password': 'testpassword123'
        }

        response = self.client.post(
            '/auth/login/',
            data=json.dumps(login_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertIn('token', response_data)
        self.assertEqual(response_data['message'], 'User logged in successfully')


class TestGetUserCardData(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            username='johndoe123',
            xp=250,
            password=make_password('testpassword123')
        )

    def test_get_user_card_data_successfully(self):
        response = self.client.get(
            f'/user_card_data/{self.test_user.user_id}/data/',
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        self.assertEqual(response_data['first_name'], 'John')
        self.assertEqual(response_data['last_name'], 'Doe')
        self.assertEqual(response_data['username'], 'johndoe123')
        self.assertEqual(response_data['xp'], 250)


class TestAddPost(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(
            email='test@example.com',
            password=make_password('testpassword123')
        )
        self.test_task = Task.objects.create(
            task_title='Test Task',
            task_description='This is a test task description',
            task_deadline='2025-12-31',
            task_xp=100,
            user=self.test_user
        )
    def test_successful_post_creation(self):
        post_data = {

            'taskId': str(self.test_task.task_id),
            'postBody': 'This is a test post'
        }

        response = self.client.post(
            f'/post/{self.test_user.user_id}/add-post/',
            data=json.dumps(post_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])

        post_exists = Post.objects.filter(
            user_id=self.test_user.user_id,
            task_id=self.test_task.task_id,
            post_body='This is a test post'
        ).exists()
        self.assertTrue(post_exists)


class TestGetAllPosts(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            password=make_password('testpassword123')
        )

        self.test_task = Task.objects.create(
            task_title='Test Task',
            task_description='This is a test task description',
            task_deadline='2025-12-31',
            task_xp=100,
            user=self.test_user
        )

        self.test_post = Post.objects.create(
            post_body='This is a test post',
            user_id=self.test_user.user_id,
            task_id=self.test_task.task_id
        )

    def test_get_posts_successfully(self):
        response = self.client.post(
            f'/post/{self.test_user.user_id}/get-all-posts/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertIn('data', response_data)
        self.assertEqual(len(response_data['data']), 1)


class TestAddTask(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            password=make_password('testpassword123')
        )

    def test_successful_task_creation(self):
        task_data = {
            'taskTitle': 'Complete Project',
            'taskDescription': 'Finish the Django project by the deadline',
            'taskDeadline': '2025-12-31',
            'taskXp': 150
        }

        response = self.client.post(
            f'/task/{self.test_user.user_id}/add-task/',
            data=json.dumps(task_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertIn('task_id', response_data)


        task_exists = Task.objects.filter(
            user=self.test_user,
            task_title='Complete Project'
        ).exists()
        self.assertTrue(task_exists)


class TestGetAllUserTasks(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            password=make_password('testpassword123')
        )

        self.test_task = Task.objects.create(
            task_title='Test Task 1',
            task_description='This is a test task description',
            task_deadline='2025-12-31',
            task_xp=100,
            user=self.test_user
        )

    def test_get_all_user_tasks_successfully(self):
        response = self.client.post(
            f'/task/{self.test_user.user_id}/get-all-tasks/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertIn('all_tasks', response_data)
        self.assertEqual(len(response_data['all_tasks']['all_tasks']), 1)


class TestCompleteTask(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            xp=0,
            password=make_password('testpassword123')
        )

        self.test_task = Task.objects.create(
            task_title='Test Task',
            task_description='This is a test task description',
            task_deadline='2025-12-31',
            task_xp=100,
            is_active=True,
            user=self.test_user
        )

    def test_complete_task_successfully(self):
        response = self.client.post(
            f'/task/{self.test_task.task_id}/complete-task/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])


        self.test_task.refresh_from_db()
        self.assertFalse(self.test_task.is_active)


        self.test_user.refresh_from_db()
        self.assertEqual(self.test_user.xp, 100)


class TestNotCompletedTask(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            xp=150,
            password=make_password('testpassword123')
        )

        self.test_task = Task.objects.create(
            task_title='Test Task',
            task_description='This is a test task description',
            task_deadline='2025-12-31',
            task_xp=100,
            is_active=False,
            user=self.test_user
        )

    def test_not_completed_task_successfully(self):
        response = self.client.post(
            f'/task/{self.test_task.task_id}/not-completed-task/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])

        self.test_task.refresh_from_db()
        self.assertTrue(self.test_task.is_active)

        self.test_user.refresh_from_db()
        self.assertEqual(self.test_user.xp, 50)


class TestDeleteTask(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            password=make_password('testpassword123')
        )

        self.test_task = Task.objects.create(
            task_title='Test Task to Delete',
            task_description='This task will be deleted',
            task_deadline='2025-12-31',
            task_xp=100,
            user=self.test_user
        )

    def test_delete_task_successfully(self):
        task_id = self.test_task.task_id

        response = self.client.post(
            f'/task/{task_id}/delete-task/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])

        task_exists = Task.objects.filter(task_id=task_id).exists()
        self.assertFalse(task_exists)
