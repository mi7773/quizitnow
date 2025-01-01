'''
tests/error/test_not_found_error_route.py

This module contains tests for handling the 404 Not Found error route
in the application.

Classes:
    NotFoundErrorRouteTestCase: Test case for the 404 Not Found error route.

Methods:
    test_get(): Tests the 404 error page when an invalid route is accessed.
'''

from tests.base import BaseTestCase


class NotFoundErrorRouteTestCase(BaseTestCase):
    '''
    Test case for the 404 Not Found error route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        """
        Tests the 404 error page when an invalid route is accessed.

        - Sends a GET request to a non-existent route '/not_found_route'.
        - Asserts that the response status code is 404.
        - Verifies that the error message in the response contains
        the appropriate message for the 404 error.
        '''

        response = self.client.get('/not_found_route')
        self.assertEqual(response.status_code, 404)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p>Oops! The page you are looking for does not exist.</p>',
                response_data
                )
