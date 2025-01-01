'''
tests/auth/test_login_route.py

This module contains tests for the login route of the authentication system.

Classes:
    LoginRouteTestCase: Test case for the login route.

Methods:
    test_get_authorized(): Tests the GET request for the login route when
    the user is already logged in.
    test_get_unauthorized(): Tests the GET request for the login route when
    the user is not logged in.
    test_post_correct_credentials(): Tests the POST request for the login route
    with correct credentials.
    test_post_wrong_password(): Tests the POST request for the login route
    with a wrong password.
    test_post_wrong_username(): Tests the POST request for the login route
    with a wrong username.
'''

from tests.base import BaseTestCase


class LoginRouteTestCase(BaseTestCase):
    '''
    Test case for the login route of the authentication system.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up the test environment by creating test users.

        Calls the parent setup method and creates test users for
        the login tests.
        '''

        super().setUp()
        self.create_test_users()

    def test_get_authorized(self):
        '''
        Tests the GET request for the login route when
        the user is already logged in.

        - Logs in as a test user.
        - Sends a GET request to the login route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        the user is already logged in.
        '''

        self.login_user(self.test_user)
        response = self.client.get('/auth/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You are already logged in.', response_data)

    def test_get_unauthorized(self):
        '''
        Tests the GET request for the login route when
        the user is not logged in.

        - Sends a GET request to the login route without being logged in.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the login form.
        '''

        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<label for=\'username\' class=\'form-label\'>\
Username</label>',
                response_data
                )

    def test_post_correct_credentials(self):
        '''
        Tests the POST request for the login route with correct credentials.

        - Sends a POST request with valid username and password.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a success message.
        '''

        response = self.client.post(
                '/auth/login',
                data={
                    'username': 'alice99',
                    'password': 'password'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('Logged in successfully!', response_data)

    def test_post_wrong_password(self):
        '''
        Tests the POST request for the login route with a wrong password.

        - Sends a POST request with the correct username but wrong password.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains an error message for
        invalid credentials.
        '''

        response = self.client.post(
                '/auth/login',
                data={
                    'username': 'alice99',
                    'password': 'wrong_password'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('Invalid username or password.', response_data)

    def test_post_wrong_username(self):
        '''
        Tests the POST request for the login route with a wrong username.

        - Sends a POST request with an invalid username and
        the correct password.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains an error message for
        invalid credentials.
        '''

        response = self.client.post(
                '/auth/login',
                data={
                    'username': 'wrong_username',
                    'password': 'password'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('Invalid username or password.', response_data)
