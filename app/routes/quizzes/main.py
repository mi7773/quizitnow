'''
app/routes/quizzes/main.py

This module defines the route for displaying a list of all quizzes.

Routes:
    /: Displays all available quizzes.

Functions:
    main: Retrieves all quizzes from the database and renders
    the quizzes list page.
'''

from app.models import Quiz
from flask import render_template
from . import quizzes_bp


@quizzes_bp.route('')
def main():
    '''
    Displays a list of all quizzes.

    This function queries the database for all quizzes
    and renders them in the quizzes main page.

    Returns:
        Response: The rendered HTML page containing a list of all quizzes.
    '''

    all_quizzes = Quiz.query.all()
    return render_template('quizzes/main.html', quizzes=all_quizzes)
