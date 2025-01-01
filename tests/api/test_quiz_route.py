'''
tests/api/test_quiz_route.py

This module contains tests for the API route that retrieves
a specific quiz's details.

Classes:
    QuizRouteTestCase: Test cases for the quiz route.

Methods:
    test_get(): Tests the retrieval of a quiz by ID from the API.
'''

from tests.base import BaseTestCase


class QuizRouteTestCase(BaseTestCase):
    '''
    Test cases for the quiz route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def test_get(self):
        '''
        Tests the retrieval of a quiz by its ID.

        - Creates a quiz and associated questions.
        - Sends a GET request to '/api/quiz/{quiz_id}'.
        - Asserts that the response status code is 200.
        - Verifies that the quiz description is correct.
        - Ensures the first question's correct option is as expected.
        '''

        self.create_test_quiz()
        self.create_test_questions()
        response = self.client.get(f'/api/quiz/{self.quiz_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn(data['description'], 'This is a sample quiz.')
        self.assertIn(
                data['questions'][0]['correct_option'],
                'a'
                )
