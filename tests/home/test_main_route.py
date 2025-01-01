'''
tests/home/test_main_route.py

This module contains tests for the main route of the home page
of the application.

Classes:
    MainRouteTestCase: Test case for the main route of the home page.

Methods:
    test_get(): Tests the GET request for the main home page route.
'''

from tests.base import BaseTestCase


class MainRouteTestCase(BaseTestCase):
    '''
    Test case for the main home page route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the GET request for the main home page route.

        - Sends a GET request to the home page route ('/').
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the introductory paragraph text
        "Test your knowledge and improve your skills!"
        '''

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p class=\'lead text-secondary\'>Test your \
knowledge and improve your skills!</p>',
                response_data
                )
