'''
add_sample_data.py

This script is used to populate the database with sample data
for the application.
It creates a sample quiz, two questions for the quiz, and two users
(one admin and one regular user).
The data is added to the respective tables in the database.

Usage:
    python add_sample_data.py

The script will:
    - Create a sample quiz with two questions.
    - Create an admin user and a regular user.
    - Add these records to the database.

Modules:
    app.extensions: The module where the database extension is initialized.
    app: The application module that contains the configuration
    and extension setup.
    app.config: The module that holds different configurations
    for the application.
    werkzeug.security: Used for securely hashing passwords.
    app.models: The module containing the database models for
    Quiz, Question, and User.

Main Functions:
    __main__: Adds sample data (quiz, questions, and users) to the database.
'''

from app.extensions import db
from app import create_app
from app.config import ProductionConfig
from werkzeug.security import generate_password_hash
from app.models import Quiz, Question, User

app = create_app(ProductionConfig)
if __name__ == '__main__':
    with app.app_context():
        '''
        Main entry point of the script. Adds sample data to the database.

        This function:
            - Creates a quiz and two questions related to the quiz.
            - Creates an admin user and a regular user with hashed passwords.
            - Adds the quiz, questions, and users to the database.
        '''

        # Create a quiz
        quiz = Quiz(title='Sample Quiz', description='This is a sample quiz.')

        db.session.add(quiz)
        db.session.commit()

        # Add questions and options
        q1 = Question(
                quiz_id=quiz.id,
                text='What is the capital of France?',
                option_a='Paris',
                option_b='London',
                option_c='Berlin',
                option_d='Madrid',
                correct_option='a'
                )

        q2 = Question(
                quiz_id=quiz.id,
                text='What is 2 + 2?',
                option_a='3',
                option_b='4',
                option_c='5',
                option_d='6',
                correct_option='b'
                )

        admin = User(
                name='Mahmoud',
                username='mi7773',
                email='mi7773@example.com',
                password=generate_password_hash(
                    password='password',
                    method='pbkdf2:sha256'
                    ),
                role='admin'
                )

        user = User(
                name='Alice',
                username='alice99',
                email='alice99@example.com',
                password=generate_password_hash(
                    password='password',
                    method='pbkdf2:sha256'
                    )
                )

        db.session.add_all([q1, q2, admin, user])
        db.session.commit()
        db.session.remove()
