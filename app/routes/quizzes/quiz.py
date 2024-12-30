'''
app/routes/quizzes/quiz.py

This module defines the route for handling individual quiz interactions.

Routes:
    /<int:quiz_id>: Handles displaying the quiz, scoring the quiz,
    and redirecting the user upon quiz completion.

Functions:
    quiz: Displays a quiz for the user to take,
    processes the results upon submission,
    and redirects the user to the dashboard.
"""
'''

from .update_results import update_results
from flask_login import login_required
from flask import request, flash, redirect, url_for, render_template
from . import quizzes_bp
from app.models import Quiz


@quizzes_bp.route('/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def quiz(quiz_id):
    '''
    Displays a quiz and handles the submission of quiz results.

    This function retrieves the quiz details using the quiz ID,
    displays the quiz for the user, and processes the
    results when the user submits their answers. Upon submission,
    the user is shown their score and redirected to
    the dashboard.

    Args:
        quiz_id (int): The ID of the quiz to be displayed.

    Returns:
        Response: 
            - If the request method is GET, it renders the quiz page
            with the quiz data.
            - If the request method is POST, it processes the results,
            flashes the score, and redirects to the dashboard.
    '''

    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        score = update_results(quiz_id, quiz)
        flash(f'You scored {score}/{len(quiz.questions)}.', 'info')
        return redirect(url_for('dashboard.main'))

    return render_template('quizzes/quiz.html', quiz=quiz)
