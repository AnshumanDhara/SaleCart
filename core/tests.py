from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_successful_login(self):
        # Simulate a POST request to the login endpoint with valid credentials
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        
        # Check if the response redirects to the homepage with a success message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login Successfull!!')

    def test_invalid_login(self):
        # Simulate a POST request to the login endpoint with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'invalid_user', 'password': 'invalid_password'})
        
        # Check if the response renders the login page again with an error message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid Username or Password!!')

    def test_get_login_page(self):
        # Simulate a GET request to the login endpoint
        response = self.client.get(reverse('login'))
        
        # Check if the response renders the login page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_successful(self):
        # Simulate a POST request with valid data
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password-confirm': 'password123'
        })

        # Check if the response redirects to the homepage with a success message
        # self.assertRedirects(response, '/homepage/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Account created successfully!!')

        # Check if the user and profile were created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_signup_passwords_not_matching(self):
        # Simulate a POST request with passwords that do not match
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password-confirm': 'password456'
        })

        # Check if the response renders the signup page with an error message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Passwords do not match!!')

        # Check if the user and profile were not created in the database
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(User.objects.filter(email='test@example.com').exists())

    # Add more test cases for other scenarios like empty fields, existing usernames, etc.
