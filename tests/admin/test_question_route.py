'''
tests/admin/test_question_route.py

This module contains tests for the question route in the admin section
of the application.

Classes:
    QuestionRouteTestCase: Test case for the question route
    in the admin section.

Methods:
    setUp(): Sets up the test environment, including creating test users,
    a test quiz, and question data.
    test_get_user(): Tests the GET request for the question route when
    the user does not have admin privileges.
    test_get_admin(): Tests the GET request for the question route when
    the user has admin privileges.
    test_post_user(): Tests the POST request for the question route when
    the user does not have admin privileges.
    test_post_admin(): Tests the POST request for the question route when
    the user has admin privileges.
'''

from tests.base import BaseTestCase


class QuestionRouteTestCase(BaseTestCase):
    '''
    Test case for the question route in the admin section.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up the test environment for question route tests.

        - Creates test users and a test quiz.
        - Initializes test data for a question.
        '''

        super().setUp()
        self.create_test_users()
        self.create_test_quiz()
        self.question_data = {
                'question_text': 'What is 2 + 2?',
                'option_a': '3',
                'option_b': '4',
                'option_c': '5',
                'option_d': '6',
                'correct_option': 'b'
                }

    def test_get_user(self):
        '''
        Tests the GET request for the question route when
        the user is not an admin.

        - Logs in as a non-admin user.
        - Sends a GET request to the question route for a quiz.
        - Asserts that the response status code is 403 (Forbidden).
        - Verifies that the response contains a permission error message.
        '''

        self.login_user(self.test_user)
        response = self.client.get(f'/admin/quiz/{self.quiz_id}/question')
        self.assertEqual(response.status_code, 403)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p>You do not have permission to access this resource.</p>',
                response_data
                )

    def test_get_admin(self):
        '''
        Tests the GET request for the question route when the user is an admin.

        - Logs in as an admin user.
        - Sends a GET request to the question route for a quiz.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the page title
        for adding a question.
        '''

        self.login_user(self.test_admin)
        response = self.client.get(f'/admin/quiz/{self.quiz_id}/question')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('<title>Add Question</title>', response_data)

    def test_post_user(self):
        '''
        Tests the POST request for the question route when
        the user is not an admin.

        - Logs in as a non-admin user.
        - Sends a POST request with question data to add a question to a quiz.
        - Asserts that the response status code is 403 (Forbidden).
        - Verifies that the response contains a permission error message.
        '''

        self.login_user(self.test_user)
        response = self.client.post(
                f'/admin/quiz/{self.quiz_id}/question',
                data=self.question_data,
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 403)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p>You do not have permission to access this resource.</p>',
                response_data
                )

    def test_post_admin(self):
        '''
        Tests the POST request for the question route when
        the user is an admin.

        - Logs in as an admin user.
        - Sends a POST request with question data to add a question to a quiz.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a success message
        indicating that the question was added.
        '''

        self.login_user(self.test_admin)
        response = self.client.post(
                f'/admin/quiz/{self.quiz_id}/question',
                data=self.question_data,
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('Question added. Add another?', response_data)
