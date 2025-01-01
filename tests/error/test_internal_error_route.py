'''
tests/error/test_internal_error_route.py

This module contains tests for handling the 500 Internal Server Error route
in the application.

Classes:
    InternalErrorRouteTestCase: Test case for
    the 500 Internal Server Error route.

Methods:
    test_get(): Tests the 500 error page when a route triggers
    an internal server error.
'''

from tests.base import BaseTestCase


class InternalErrorRouteTestCase(BaseTestCase):
    '''
    Test case for the 500 Internal Server Error route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the 500 error page when a route triggers
        an internal server error.

        - Sends a GET request to a route '/cause_error' that causes
        an internal error.
        - Asserts that the response status code is 500.
        - Verifies that the error message in the response contains
        the appropriate message for the 500 error.
        '''

        response = self.client.get('/cause_error')
        self.assertEqual(response.status_code, 500)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p>Something went wrong on our end. \
Please try again later.</p>',
                response_data
                )
