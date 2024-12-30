'''
app/routes/admin/quiz.py

This module defines the route for adding a new quiz.

Functions:
    quiz(): Handles the form for creating a new quiz and redirecting
    to the question addition page.
'''

from . import admin_bp
from flask_login import current_user, login_required
from flask import request, redirect, url_for, render_template, flash
from .add_quiz import add_quiz


@admin_bp.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    '''
    Handles the process of adding a new quiz.

    This function checks if the current user has the 'admin' role.
    If the user is an admin,
    the function processes a form submission for creating a new quiz
    and redirects to the
    question creation page with a flash message. If the form is not submitted,
    it displays the quiz creation form.

    Args:
        None

    Returns:
        Response: A rendered template of the quiz creation form
        or a redirect after the form submission.
    '''

    if current_user.role == 'admin':
        if request.method == 'POST':
            quiz_id = add_quiz()
            flash('New quiz added successfully!', 'success')
            return redirect(url_for('admin.question', quiz_id=quiz_id))
        return render_template('admin/quiz.html')
    return render_template('error/403.html'), 403
