'''
tests/quizzes/test_main_route.py

This module contains tests for the main route of the quizzes page.

Classes:
    MainRouteTestCase: Test case for the main route of the quizzes page.

Methods:
    test_get(): Tests the GET request for the main quizzes page route.
'''

from tests.base import BaseTestCase


class MainRouteTestCase(BaseTestCase):
    '''
    Test case for the main quizzes page route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the GET request for the main quizzes page route.

        - Sends a GET request to the quizzes page route ('/quizzes').
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the title "Available Quizzes".
        '''

        response = self.client.get('/quizzes')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('<title>Available Quizzes</title>', response_data)
