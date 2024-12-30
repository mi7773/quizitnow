'''
app/routes/quizzes/__init__.py

This module initializes the quizzes blueprint and imports the related routes.

Blueprint:
    quizzes_bp: A blueprint for handling all routes related to quizzes.

Modules:
    quiz: Defines the route for handling individual quiz interactions.
    main: Defines the main route for displaying a list of all quizzes.
'''

from flask import Blueprint

quizzes_bp = Blueprint('quizzes', __name__, url_prefix='/quizzes')

from .quiz import quiz  # noqa: E402
from .main import main  # noqa: E402
