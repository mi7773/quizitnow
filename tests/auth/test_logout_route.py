'''
tests/auth/test_logout_route.py

This module contains tests for the logout route of the authentication system.

Classes:
    LogoutRouteTestCase: Test case for the logout route.

Methods:
    test_get_unauthorized(): Tests the GET request for the logout route when
    the user is not logged in.
    test_get_authorized(): Tests the GET request for the logout route when
    the user is logged in.
'''

from tests.base import BaseTestCase


class LogoutRouteTestCase(BaseTestCase):
    '''
    Test case for the logout route of the authentication system.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get_unauthorized(self):
        '''
       Tests the GET request for the logout route when
       the user is not logged in.

        - Sends a GET request to the logout route without being logged in.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        that the user is not logged in.
        '''

        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You are not logged in.', response_data)

    def test_get_authorized(self):
        '''
        Tests the GET request for the logout route when the user is logged in.

        - Creates test users and logs in as a test user.
        - Sends a GET request to the logout route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        that the user has been logged out.
        '''

        self.create_test_users()
        self.login_user(self.test_user)
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You have been logged out.', response_data)
