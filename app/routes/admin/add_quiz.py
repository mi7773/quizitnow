'''
app/routes/admin/add_quiz.py

This module defines the function for adding a new quiz to the system.

Functions:
    add_quiz(): Adds a new quiz to the database
    with the provided title and description.

Returns:
    int: The ID of the newly created quiz.
'''

from flask import request
from app.models import Quiz
from app.extensions import db


def add_quiz():
    '''
    Adds a new quiz to the database.

    This function retrieves the quiz title and description
    from the form request,
    creates a new `Quiz` object, adds it to the database,
    and commits the transaction.

    Returns:
        int: The ID of the newly created quiz.
    '''

    title = request.form['title']
    description = request.form['description']
    quiz = Quiz(title=title, description=description)
    db.session.add(quiz)
    db.session.commit()
    return quiz.id
