'''
app/routes/dashboard/leaderboard.py

This module defines the route for displaying the leaderboard in the dashboard.
The leaderboard shows the top 10 users based on their quiz scores (percentage).

Routes:
    - leaderboard: Displays the leaderboard with the top 10 users' scores.
'''

from flask import render_template
from app.models import QuizResult
from . import dashboard_bp
from flask_login import login_required


@dashboard_bp.route('/leaderboard')
@login_required
def leaderboard():
    '''
    Renders the leaderboard page with the top 10 highest quiz scores.

    The leaderboard is ordered by the percentage of correct answers and
    shows the top 10 results.

    Returns:
        render_template: The rendered leaderboard HTML page.
    '''

    scores = QuizResult.query.order_by(
            QuizResult.percent.desc()
            ).limit(10).all()
    return render_template('dashboard/leaderboard.html', scores=scores)
