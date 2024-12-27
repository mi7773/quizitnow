'''
models/question.py

This module defines the Question model for a Flask application.

Classes:
    Question: Represents a question in a quiz, with options
    and a correct answer.

Attributes:
    id (int): Primary key for the question.
    quiz_id (int): Foreign key referencing the quiz this question belongs to.
    text (str): The question text.
    option_a (str): Option A for the question.
    option_b (str): Option B for the question.
    option_c (str): Option C for the question.
    option_d (str): Option D for the question.
    correct_option (str): Indicates the correct option ('a', 'b', 'c', or 'd').
'''

from app.extensions import db
from flask_login import UserMixin
from datetime import datetime


class Question(db.Model):
    '''
    Represents a question in a quiz.

    Attributes:
        id (int): Unique identifier for the question.
        quiz_id (int): Identifier of the related quiz.
        text (str): Text content of the question.
        option_a (str): First option.
        option_b (str): Second option.
        option_c (str): Third option.
        option_d (str): Fourth option.
        correct_option (str): Correct answer ('a', 'b', 'c', or 'd').
    '''

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # a, b, c, or d
