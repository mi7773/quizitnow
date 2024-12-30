'''
app/routes/dashboard/old.py

This module defines the route for the old quizzes page on the dashboard.
It shows the quizzes that the current user has already taken,
along with their scores.

Routes:
    - old: Displays a list of quizzes the user has already completed,
    along with their respective scores.
'''

from . import dashboard_bp
from flask import render_template
from flask_login import current_user, login_required
from app.models import QuizResult, Quiz


@dashboard_bp.route('/old')
@login_required
def old():
    '''
    Renders a list of quizzes that the logged-in user has already taken,
    along with their respective scores.

    The quizzes are filtered to include only those the current user
    has completed, and the scores are displayed alongside the quizzes.

    Returns:
        render_template: The rendered HTML page displaying the old quizzes
        and their corresponding scores.
    '''

    results = QuizResult.query.filter_by(user_id=current_user.id)
    quizzes = Quiz.query.all()
    old_id = [result.quiz_id for result in results]
    old = [quiz for quiz in quizzes if quiz.id in old_id][::-1]
    score = {result.quiz_id: result.score for result in results}
    return render_template('dashboard/old.html', old=old, score=score)
