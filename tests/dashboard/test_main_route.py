'''
tests/dashboard/test_main_route.py

This module contains tests for the main dashboard route of the application.

Classes:
    MainRouteTestCase: Test case for the main dashboard route.

Methods:
    test_get_unauthorized(): Tests the GET request for the dashboard when
    the user is not logged in.
    test_get_authorized(): Tests the GET request for the dashboard when
    the user is logged in.
'''

from tests.base import BaseTestCase


class MainRouteTestCase(BaseTestCase):
    '''
    Test case for the main dashboard route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get_unauthorized(self):
        '''
        Tests the GET request for the dashboard when the user is not logged in.

        - Sends a GET request to the dashboard route without being logged in.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        the user needs to be registered to access the page.
        '''

        response = self.client.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'You must register in to access this page.',
                response_data
                )

    def test_get_authorized(self):
        '''
        Tests the GET request for the dashboard when the user is logged in.

        - Creates a test user and logs them in.
        - Sends a GET request to the dashboard route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the "New Quizzes" card title.
        '''

        self.create_test_users()
        self.login_user(self.test_user)
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<h5 class=\'card-title\'>New Quizzes</h5>',
                response_data
                )
