'''
tests/api/test_question_route.py

This module contains tests for the API route handling questions in
the Flask application.

Classes:
    QuestionRouteTestCase: Test cases for the question API route.

Methods:
    test_get(): Tests the GET request to retrieve a specific question by ID.
'''

from tests.base import BaseTestCase


class QuestionRouteTestCase(BaseTestCase):
    '''
    Test cases for the question API route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the GET request to retrieve a specific question by its ID.

        - Verifies that the API responds with a 200 status code.
        - Asserts that the returned question data matches the expected values.
        '''
        self.create_test_quiz()
        self.create_test_questions()
        response = self.client.get(f'/api/question/{self.q1_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['correct_option'], 'a')
        self.assertEqual(data['option_d'], 'Madrid')
