'''
app/models/__init__.py

This module imports the models for the Flask application to make them
accessible from the `models` package.

It imports the following models:
    - User: Represents a user in the system.
    - Quiz: Represents a quiz in the system.
    - Question: Represents a question in a quiz.
    - QuizResult: Represents the result of a user taking a quiz.
'''

from .user import User
from .quiz import Quiz
from .question import Question
from .quiz_result import QuizResult
