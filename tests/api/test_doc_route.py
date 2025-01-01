'''
tests/api/test_doc_route.py

This module contains tests for the API route that serves the documentation
page in the Flask application.

Classes:
    DocRouteTestCase: Test cases for the API documentation route.

Methods:
    test_get(): Tests the API documentation route for successful response
    and content.
'''

from tests.base import BaseTestCase


class DocRouteTestCase(BaseTestCase):
    '''
    Test cases for the API documentation route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the API documentation route.

        - Sends a GET request to '/api/doc'.
        - Asserts that the response status code is 200.
        - Verifies that the response contains the expected HTML
        content indicating the API documentation page.
        '''

        response = self.client.get('/api/doc')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('<title>API Documentation</title>', response_data)
