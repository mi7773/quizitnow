'''
tests/base.py

This module provides a base test case class for the Flask application.

Classes:
    BaseTestCase: A base class for setting up and tearing down
    the testing environment,
    including helper methods for creating test data and handling
    user authentication.

Methods:
    setUp(): Prepares the testing environment, including initializing
    the Flask app context,
    database setup, and configuring the test client.
    tearDown(): Cleans up the testing environment by removing the database
    session and disposing of resources.
    create_test_quiz(): Creates a sample quiz entry in the database.
    create_test_questions(): Creates sample question entries linked
    to a quiz in the database.
    create_test_users(): Creates sample user entries (admin and regular user)
    in the database.
    login_user(user): Logs in a user to the test client.
    logout_user(): Logs out the currently logged-in user from the test client.
'''

import unittest
from app.extensions import db
from app import create_app
from app.config import TestingConfig
from werkzeug.security import generate_password_hash
from app.models import User, Quiz, Question
import warnings
from sqlalchemy.exc import LegacyAPIWarning


class BaseTestCase(unittest.TestCase):
    '''
    A base class for Flask application tests.

    Provides a controlled environment for unit tests by setting up and tearing
    down the database, app context, and other necessary resources.
    '''

    def setUp(self):
        '''
        Sets up the test environment.

        - Ignores deprecation and legacy warnings.
        - Initializes the Flask app with testing configurations.
        - Pushes the app context and sets up the test database.
        '''

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        warnings.filterwarnings('ignore', category=LegacyAPIWarning)

        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.client.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        '''
        Cleans up the test environment.

        - Removes the database session and drops all tables.
        - Disposes of the database engine and pops the app context.
        '''

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        self.app_context.pop()

    def create_test_quiz(self):
        '''
        Creates a sample quiz in the database.

        Attributes:
            self.test_quiz (Quiz): The created quiz object.
            self.quiz_id (int): The ID of the created quiz.
        '''

        self.test_quiz = Quiz(
                title='Sample Quiz',
                description='This is a sample quiz.'
                )
        db.session.add(self.test_quiz)
        db.session.commit()
        self.quiz_id = self.test_quiz.id

    def create_test_questions(self):
        '''
        Creates sample questions linked to the test quiz.

        Attributes:
            self.test_q1 (Question): First test question object.
            self.test_q2 (Question): Second test question object.
            self.q1_id (int): ID of the first test question.
            self.q2_id (int): ID of the second test question.
        '''

        self.test_q1 = Question(
                quiz_id=self.quiz_id,
                text='What is the capital of France?',
                option_a='Paris',
                option_b='London',
                option_c='Berlin',
                option_d='Madrid',
                correct_option='a'
                )
        self.test_q2 = Question(
                quiz_id=self.quiz_id,
                text='What is 2 + 2?',
                option_a='3',
                option_b='4',
                option_c='5',
                option_d='6',
                correct_option='b'
                )
        db.session.add_all([self.test_q1, self.test_q2])
        db.session.commit()
        self.q1_id = self.test_q1.id
        self.q2_id = self.test_q2.id

    def create_test_users(self):
        '''
        Creates sample users in the database.

        Attributes:
            self.test_admin (User): Test admin user object.
            self.test_user (User): Test regular user object.
        '''

        self.test_admin = User(
                name='Mahmoud',
                username='mi7773',
                email='mi7773@example.com',
                password=generate_password_hash(
                    password='password',
                    method='pbkdf2:sha256'
                    ),
                role='admin'
                )
        self.test_user = User(
                name='Alice',
                username='alice99',
                email='alice99@example.com',
                password=generate_password_hash(
                    password='password',
                    method='pbkdf2:sha256'
                    )
                )
        db.session.add_all([self.test_admin, self.test_user])
        db.session.commit()

    def login_user(self, user):
        '''
        Logs in the specified user to the test client.

        Args:
            user (User): The user to log in.
        '''

        login_data = {
                'username': user.username,
                'password': 'password'
                }
        self.client.post(
                'auth/login',
                data=login_data,
                follow_redirects=True
                )

    def logout_user(self):
        '''
        Logs out the currently logged-in user from the test client.
        '''

        self.client.get('auth/logout')
