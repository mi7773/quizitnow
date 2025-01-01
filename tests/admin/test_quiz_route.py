'''
tests/admin/test_quiz_route.py

This module contains tests for the quiz route in the admin section
of the application.

Classes:
    QuizRouteTestCase: Test case for the quiz route in the admin section.

Methods:
    setUp(): Sets up the test environment, including creating test users
    and initializing quiz data.
    test_get_user(): Tests the GET request for the quiz route when
    the user does not have admin privileges.
    test_get_admin(): Tests the GET request for the quiz route when
    the user has admin privileges.
    test_post_user(): Tests the POST request for the quiz route when
    the user does not have admin privileges.
    test_post_admin(): Tests the POST request for the quiz route when
    the user has admin privileges.
'''

from tests.base import BaseTestCase


class QuizRouteTestCase(BaseTestCase):
    '''
    Test case for the quiz route in the admin section.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up the test environment for quiz route tests.

        - Creates test users and initializes quiz data.
        '''

        super().setUp()
        self.create_test_users()
        self.quiz_data = {
                'title': 'Sample Quiz',
                'description': 'This is a sample quiz.'
                }

    def test_get_user(self):
        '''
        Tests the GET request for the quiz route when the user is not an admin.

        - Logs in as a non-admin user.
        - Sends a GET request to the quiz route.
        - Asserts that the response status code is 403 (Forbidden).
        - Verifies that the response contains a permission error message.
        '''

        self.login_user(self.test_user)
        response = self.client.get('/admin/quiz')
        self.assertEqual(response.status_code, 403)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<p>You do not have permission to access this resource.</p>',
                response_data
                )

    def test_get_admin(self):
        '''
        Tests the GET request for the quiz route when the user is an admin.

        - Logs in as an admin user.
        - Sends a GET request to the quiz route.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains the page title for
        adding a new quiz.
        '''

        self.login_user(self.test_admin)
        response = self.client.get('/admin/quiz')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<h2 class=\'mb-4\'>Add New Quiz</h2>',
                response_data
                )

    def test_post_user(self):
        '''
        Tests the POST request for the quiz route when
        the user is not an admin.

        - Logs in as a non-admin user.
        - Sends a POST request with quiz data to add a new quiz.
        - Asserts that the response status code is 403 (Forbidden).
        - Verifies that the response contains a permission error message.
        '''

        self.login_user(self.test_user)
        response = self.client.post(
                '/admin/quiz',
                data=self.quiz_data,
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
        Tests the POST request for the quiz route when the user is an admin.

        - Logs in as an admin user.
        - Sends a POST request with quiz data to add a new quiz.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a success message
        indicating that the quiz was added.
        '''

        self.login_user(self.test_admin)
        response = self.client.post(
                '/admin/quiz',
                data=self.quiz_data,
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('New quiz added successfully!', response_data)
