'''
app/routes/admin/question.py

This module defines the route for adding questions to a quiz.

Functions:
    question(quiz_id): Handles displaying and processing
    the form for adding questions to a specific quiz.
'''

from . import admin_bp
from flask_login import login_required, current_user
from flask import request, flash, redirect, url_for, render_template
from .add_question import add_question
from app.models import Quiz


@admin_bp.route('/quiz/<int:quiz_id>/question', methods=['GET', 'POST'])
@login_required
def question(quiz_id):
    '''
    Handles the process of adding a new question to a quiz.

    This function checks if the current user has the 'admin' role,
    retrieves the quiz based on its ID,
    and processes a form to add a new question to the quiz.
    If the form is submitted, it calls
    `add_question()` to save the new question and then
    redirects the user to the same page
    with a flash message confirming the addition.

    Args:
        quiz_id (int): The ID of the quiz to which the question will be added.

    Returns:
        Response: A rendered template of the question form,
        or a redirect after the form submission.
    '''

    if current_user.role == 'admin':
        quiz = Quiz.query.get_or_404(quiz_id)
        if request.method == 'POST':
            add_question(quiz.id)
            flash('Question added. Add another?', 'success')
            return redirect(url_for('admin.question', quiz_id=quiz_id))
        return render_template('admin/question.html', quiz=quiz)
    return render_template('error/403.html'), 403
