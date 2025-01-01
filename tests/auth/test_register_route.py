'''
tests/auth/test_register_route.py

This module contains tests for the registration route
of the authentication system.

Classes:
    RegisterRouteTestCase: Test case for the registration route.

Methods:
    test_get_unauthorized(): Tests the GET request for
    the registration route when the user is not logged in.
    test_get_authorized(): Tests the GET request for
    the registration route when the user is already logged in.
    test_post_correct_credentials(): Tests the POST request for
    the registration route with valid registration data.
    test_post_used_email(): Tests the POST request for
    the registration route with an already used email.
    test_post_used_username(): Tests the POST request for
    the registration route with an already used username.
'''

from tests.base import BaseTestCase


class RegisterRouteTestCase(BaseTestCase):
    '''
    Test case for the registration route of the authentication system.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get_unauthorized(self):
        '''
        Tests the GET request for the registration route when
        the user is not logged in.

        - Sends a GET request to the registration route without
        being logged in.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the registration form.
        '''

        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<label for=\'First_name\' class=\'form-label\'>\
First name</label>',
                response_data)

    def test_get_authorized(self):
        '''
        Tests the GET request for the registration route when
        the user is already logged in.

        - Logs in as a test user.
        - Sends a GET request to the registration route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        the user is already logged in.
        '''

        self.create_test_users()
        self.login_user(self.test_user)
        response = self.client.get('/auth/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You are already logged in.', response_data)

    def test_post_correct_credentials(self):
        '''
        Tests the POST request for the registration route with
        valid registration data.

        - Sends a POST request with valid registration information
        (first name, username, email, password).
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a success message.
        '''

        response = self.client.post(
                '/auth/register',
                data={
                    'first_name': 'Mahmoud',
                    'username': 'mi7773',
                    'email': 'mi7773@example.com',
                    'password': 'password'
                    },
                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('Registration successful.', response_data)

    def test_post_used_email(self):
        '''
        Tests the POST request for the registration route with
        an already used email.

        - Creates test users with existing email.
        - Sends a POST request with the same email address for registration.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains an error message for
        the already used email.
        '''

        self.create_test_users()
        response = self.client.post(
                '/auth/register',
                data={
                    'first_name': 'Mahmoud',
                    'username': 'mismail7773',
                    'email': 'mi7773@example.com',
                    'password': 'password'
                    },
                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'The username or email is already in use.',
                response_data
                )

    def test_post_used_username(self):
        '''
        Tests the POST request for the registration route with
        an already used username.

        - Creates test users with existing username.
        - Sends a POST request with the same username for registration.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains an error message for
        the already used username.
        '''

        self.create_test_users()
        response = self.client.post(
                '/auth/register',
                data={
                    'first_name': 'Mahmoud',
                    'username': 'mi7773',
                    'email': 'mismail7773@example.com',
                    'password': 'password'
                    },
                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'The username or email is already in use.',
                response_data
                )
