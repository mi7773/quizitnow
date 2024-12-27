'''
models/quiz.py

Classes:
    Quiz: Represents a quiz with a title, description, and related questions.

Attributes:
    id (int): Primary key for the quiz.
    title (str): The title of the quiz.
    description (str): The description of the quiz.
    questions (list): List of related questions for the quiz.
'''

from app.extensions import db
from flask_login import UserMixin
from datetime import datetime


class Quiz(db.Model):
    '''
    Represents a quiz in the system.

    Attributes:
        id (int): Unique identifier for the quiz.
        title (str): Title of the quiz.
        description (str): Description of the quiz.
        questions (list): List of Question objects related to the quiz.
    '''

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    questions = db.relationship('Question')
