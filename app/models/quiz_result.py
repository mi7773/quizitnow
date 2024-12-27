'''
app/models/quiz_result.py

This module defines the QuizResult model for a Flask application.

Classes:
    QuizResult: Represents the result of a user taking a quiz,
    including score, percent, and timestamp.

Attributes:
    id (int): Primary key for the quiz result.
    user_id (int): Foreign key referencing the user who took the quiz.
    quiz_id (int): Foreign key referencing the quiz taken by the user.
    score (int): Score obtained by the user in the quiz.
    percent (int): Percent score obtained by the user.
    timestamp (datetime): Timestamp when the result was created or updated.
    user (User): The user who took the quiz.
    quiz (Quiz): The quiz that the user took.
'''

from app.extensions import db
from flask_login import UserMixin
from datetime import datetime


class QuizResult(db.Model):
    '''
    Represents the result of a user taking a quiz.

    Attributes:
        id (int): Unique identifier for the quiz result.
        user_id (int): Identifier of the user who took the quiz.
        quiz_id (int): Identifier of the quiz taken by the user.
        score (int): Score obtained by the user.
        percent (int): Percent score obtained by the user.
        timestamp (datetime): The timestamp when the result was created
        or updated.
        user (User): The user who took the quiz.
        quiz (Quiz): The quiz that the user took.
    '''

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    percent = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(
            db.DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow
            )
    user = db.Relationship('User')
    quiz = db.Relationship('Quiz')
