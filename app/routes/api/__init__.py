'''
app/routes/api/__init__.py

This module initializes the `api` blueprint for the Flask application.

Blueprint:
    api_bp: The blueprint for API routes, prefixed with `/api`.

Imports:
    - quizzes: API routes related to quizzes.
    - quiz: API routes for individual quizzes.
    - question: API routes for questions.
    - doc: API routes for API documentation.
'''

from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')

from .quizzes import quizzes  # noqa: E402
from .quiz import quiz  # noqa: E402
from .question import question  # noqa: E402
from .doc import doc  # noqa: E402
