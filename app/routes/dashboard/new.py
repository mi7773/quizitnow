'''
app/routes/dashboard/new.py

This module defines the route for the new quizzes page on the dashboard.
It shows the quizzes that the current user has not taken yet.

Routes:
    - new: Displays a list of new quizzes for the logged-in user,
    excluding quizzes they have already completed.
'''

from . import dashboard_bp
from flask import render_template
from flask_login import login_required, current_user
from app.models import QuizResult, Quiz


@dashboard_bp.route('/new')
@login_required
def new():
    '''
    Renders a list of new quizzes that the logged-in user has not yet taken.

    The quizzes are filtered to exclude those that the current user has already
    completed, and the remaining quizzes are displayed in reverse order.

    Returns:
        render_template: The rendered HTML page displaying the new quizzes.
    '''

    results = QuizResult.query.filter_by(user_id=current_user.id)
    quizzes = Quiz.query.all()
    old_id = [result.quiz_id for result in results]
    new = [quiz for quiz in quizzes if quiz.id not in old_id][::-1]
    return render_template('dashboard/new.html', new=new)
