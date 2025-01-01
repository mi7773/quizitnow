'''
tests/api/test_quizzes_route.py

This module contains tests for the API route handling quizzes
in the Flask application.

Classes:
    QuizzesRouteTestCase: Test cases for the quizzes API route.

Methods:
    setUp(): Sets up test data including multiple quizzes and questions.
    test_get_with_pagination(): Tests retrieving quizzes
    with pagination parameters.
    test_get_without_pagination(): Tests retrieving quizzes
    without pagination parameters.
'''

from tests.base import BaseTestCase


class QuizzesRouteTestCase(BaseTestCase):
    '''
    Test cases for the quizzes API route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up test data including multiple quizzes and associated questions.
        '''

        super().setUp()
        self.create_test_quiz()
        self.create_test_questions()
        self.create_test_questions()
        self.create_test_questions()
        self.create_test_quiz()
        self.create_test_questions()
        self.create_test_questions()
        self.create_test_quiz()
        self.create_test_questions()

    def test_get_with_pagination(self):
        '''
       Tests retrieving quizzes with pagination parameters.

        - Sends a GET request with page and per_page parameters.
        - Verifies the response includes pagination details and
        the correct quiz data.
        '''

        response = self.client.get('/api/quizzes?page=2&per_page=2')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['current_page'], 2)
        self.assertEqual(data['total'], 3)
        self.assertEqual(data['pages'], 2)
        self.assertEqual(
                data['quizzes'][0]['description'],
                'This is a sample quiz.'
                )

    def test_get_without_pagination(self):
        '''
        Tests retrieving quizzes without pagination parameters.

        - Sends a GET request without specifying page or per_page.
        - Verifies the response contains all quizzes and the correct data.
        '''

        response = self.client.get('/api/quizzes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total'], 3)
        self.assertEqual(
                data['quizzes'][0]['description'],
                'This is a sample quiz.'
                )
