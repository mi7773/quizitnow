'''
tests/dashboard/test_new_route.py

This module contains tests for the "new" dashboard route of the application,
which allows users to access new quizzes.

Classes:
    NewRouteTestCase: Test case for the "new" route in the dashboard.

Methods:
    test_get_unauthorized(): Tests the GET request for the new quizzes route
    when the user is not logged in.
    test_get_authorized(): Tests the GET request for the new quizzes route
    when the user is logged in.
'''

from tests.base import BaseTestCase


class NewRouteTestCase(BaseTestCase):
    '''
    Test case for the "new" dashboard route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get_unauthorized(self):
        '''
        Tests the GET request for the "new" quizzes route when
        the user is not logged in.

        - Sends a GET request to the new quizzes route without being logged in.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        the user must be registered to access the page.
        '''

        response = self.client.get('/dashboard/new', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'You must register in to access this page.',
                response_data
                )

    def test_get_authorized(self):
        '''
        Tests the GET request for the "new" quizzes route when
        the user is logged in.

        - Creates a test user and logs them in.
        - Sends a GET request to the new quizzes route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the "New Quizzes" heading.
        '''

        self.create_test_users()
        self.login_user(self.test_user)
        response = self.client.get('/dashboard/new')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<h1 class=\'text-center mb-4\'>New Quizzes</h1>',
                response_data
                )
