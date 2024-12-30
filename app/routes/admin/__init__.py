'''
app/routes/admin/__init__.py

This module initializes the Blueprint for the admin routes
and imports the related route handlers.

Blueprints:
    admin_bp: The Blueprint for the admin panel routes.

Route Handlers:
    quiz: Handles the quiz-related administrative functions.
    question: Handles the question-related administrative functions.
'''

from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

from .quiz import quiz  # noqa: E402
from .question import question  # noqa: E402
