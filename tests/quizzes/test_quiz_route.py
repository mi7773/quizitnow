'''
tests/quizzes/test_quiz_route.py

This module contains tests for the quiz route, which includes viewing a quiz,
submitting quiz answers, and checking user responses.

Classes:
    QuizRouteTestCase: Test case for the quiz page route.

Methods:
    test_get_authorized(): Tests accessing the quiz page when logged in.
    test_get_unauthorized(): Tests accessing the quiz page when not logged in.
    test_full_mark(): Tests submitting the correct answers and
    scoring full marks.
    test_zero(): Tests submitting incorrect answers and scoring zero.
'''

from tests.base import BaseTestCase


class QuizRouteTestCase(BaseTestCase):
    '''
    Test case for the quiz page route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up the test environment by creating a quiz, questions,
        and test users,
        then logging in a test user.
        '''

        super().setUp()
        self.create_test_quiz()
        self.create_test_questions()
        self.create_test_users()
        self.login_user(self.test_user)

    def test_get_authorized(self):
        '''
        Tests accessing the quiz page when logged in.

        - Sends a GET request to the quiz page route with a valid quiz ID.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the page contains the quiz title (e.g., "Sample Quiz").
        '''

        response = self.client.get(f'/quizzes/{self.quiz_id}')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('<h2>Sample Quiz</h2>', response_data)

    def test_get_unauthorized(self):
        '''
        Tests accessing the quiz page when not logged in.

        - Logs out the test user.
        - Sends a GET request to the quiz page route with a valid quiz ID.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the page contains a "Register" prompt for
        unauthorized users.
        '''
        self.logout_user()
        response = self.client.get(
                f'/quizzes/{self.quiz_id}',
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('<h2 class=\'text-center\'>Register</h2>', response_data)

    def test_full_mark(self):
        '''
        Tests submitting the correct answers and scoring full marks.

        - Sends a POST request with correct answers for all quiz questions.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        a perfect score.
        '''

        response = self.client.post(
                f'/quizzes/{self.quiz_id}',
                data={
                    f'{self.q1_id}': 'A',
                    f'{self.q2_id}': 'B'
                    },
                follow_redirects=True
                    )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You scored 2/2.', response_data)

    def test_zero(self):
        '''
        Tests submitting incorrect answers and scoring zero.

        - Sends a POST request with incorrect answers for all quiz questions.
        - Asserts that the response status code is 200 (OK).
        - Verifies that the response contains a message indicating
        a score of zero.
        '''

        response = self.client.post(
                f'/quizzes/{self.quiz_id}',
                data={
                    f'{self.q1_id}': 'B',
                    f'{self.q2_id}': 'C'
                    },
                follow_redirects=True
                    )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn('You scored 0/2.', response_data)
