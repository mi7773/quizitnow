'''
app/routes/dashboard/__init__.py

This module initializes the dashboard blueprint and registers the routes
associated with the dashboard section of the application.

Routes:
    - main: Displays the main dashboard view.
    - new: Displays the new quizzes section of the dashboard.
    - old: Displays the old quizzes section of the dashboard.
    - leaderboard: Displays the leaderboard page.

Blueprint:
    dashboard_bp: The blueprint for managing routes related to the dashboard.
'''

from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

from .main import main  # noqa: E402
from .new import new  # noqa: E402
from .old import old  # noqa: E402
from .leaderboard import leaderboard  # noqa: E402
