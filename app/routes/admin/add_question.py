'''
app/routes/admin/add_question.py

This module defines the function for adding a new question to a specific quiz.

Functions:
    add_question(quiz_id): Adds a new question to the specified quiz
    with the provided data.

Args:
    quiz_id (int): The ID of the quiz to which the question will be added.
'''

from app.models import Question
from flask import request
from app.extensions import db


def add_question(quiz_id):
    '''
    Adds a new question to the specified quiz.

    This function creates a new `Question` object using the data
    from the form request,
    adds it to the database, and commits the transaction.

    Args:
        quiz_id (int): The ID of the quiz to which the question will be added.
    '''

    question = Question(
            text=request.form['question_text'],
            option_a=request.form['option_a'],
            option_b=request.form['option_b'],
            option_c=request.form['option_c'],
            option_d=request.form['option_d'],
            correct_option=request.form['correct_option'].lower(),
            quiz_id=quiz_id,
            )
    db.session.add(question)
    db.session.commit()
