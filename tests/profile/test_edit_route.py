'''
tests/profile/test_edit_route.py

This module contains tests for the profile editing route in the application.

Classes:
    EditRouteTestCase: Test case for the profile edit route.

Methods:
    setUp(): Sets up the test environment, including creating
    test users and logging in a test user.
    test_get_unauthorized(): Tests the GET request for
    the edit profile page when the user is not logged in.
    test_get_authorized(): Tests the GET request for
    the edit profile page when the user is logged in.
    test_post_unauthorized(): Tests the POST request for
    the edit profile page when the user is not logged in.
    test_post_used_username(): Tests the POST request for
    the edit profile page when the username already exists.
    test_post_used_email(): Tests the POST request for
    the edit profile page when the email already exists.
    test_post_correct_changes(): Tests the POST request for
    the edit profile page when valid changes are made.
'''

from tests.base import BaseTestCase


class EditRouteTestCase(BaseTestCase):
    '''
    Test case for the profile edit route.

    Inherits:
        BaseTestCase: Provides setup, teardown, and helper methods for testing.
    '''

    def setUp(self):
        '''
        Sets up the test environment for profile edit tests.

        - Creates test users.
        - Logs in the test user.
        '''

        super().setUp()
        self.create_test_users()
        self.login_user(self.test_user)

    def test_get_unauthorized(self):
        '''
        Tests the GET request for the edit profile page when the user
        is not logged in.

        - Logs out the user.
        - Sends a GET request to the '/profile/edit' route.
        - Asserts that the response status code is 200.
        - Verifies that the response contains the message indicating
        the user needs to log in.
        '''

        self.logout_user()
        response = self.client.get('/profile/edit', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'You must register in to access this page.',
                response_data
                )

    def test_get_authorized(self):
        '''
        Tests the GET request for the edit profile page when
        the user is logged in.

        - Sends a GET request to the '/profile/edit' route.
        - Asserts that the response contains the profile edit form
        with the 'First Name' label.
        '''

        response = self.client.get('/profile/edit')
        response_data = response.data.decode('utf-8')
        self.assertIn(
                '<label for=\'First_name\' \
class=\'form-label\'>First Name</label>',
                response_data
                )

    def test_post_unauthorized(self):
        '''
        Tests the POST request for the edit profile page when
        the user is not logged in.

        - Logs out the user.
        - Sends a POST request with updated profile data.
        - Asserts that the response status code is 200.
        - Verifies that the response contains the message indicating
        the user needs to log in.
        '''

        self.logout_user()
        response = self.client.post(
                '/profile/edit',
                data={
                    'first_name': 'Mahmoud',
                    'username': 'mi7773',
                    'email': 'mi7773@example.com'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'You must register in to access this page.',
                response_data
                )

    def test_post_used_username(self):
        '''
        Tests the POST request for the edit profile page when
        the username already exists.

        - Sends a POST request with a username that already exists.
        - Asserts that the response status code is 200.
        - Verifies that the response contains the message about
        the username being already taken.
        '''

        response = self.client.post(
                '/profile/edit',
                data={
                    'first_name': 'Alice',
                    'username': 'mi7773',
                    'email': 'alice99@example.com'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'Username already exists.',
                response_data
                )

    def test_post_used_email(self):
        '''
        Tests the POST request for the edit profile page when
        the email already exists.

        - Sends a POST request with an email that already exists.
        - Asserts that the response status code is 200.
        - Verifies that the response contains the message about
        the email being already taken.
        '''

        response = self.client.post(
                '/profile/edit',
                data={
                    'first_name': 'Alice',
                    'username': 'alice99',
                    'email': 'mi7773@example.com'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'Email already exists.',
                response_data
                )

    def test_post_correct_changes(self):
        '''
        Tests the POST request for the edit profile page when
        valid changes are made.

        - Sends a POST request with valid updated profile data.
        - Asserts that the response status code is 200.
        - Verifies that the response contains a success message
        indicating the changes were saved.
        '''

        response = self.client.post(
                '/profile/edit',
                data={
                    'first_name': 'Alice',
                    'username': 'alice88',
                    'email': 'alice88@example.com'
                    },
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn(
                'Changes saved!',
                response_data
                )
