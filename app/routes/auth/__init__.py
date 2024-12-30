'''
app/routes/auth/__init__.py

This module initializes the auth blueprint for the Flask application,
responsible for authentication-related routes.

Blueprint:
    auth_bp: The blueprint for the authentication routes, including login,
    logout, and registration.
'''

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from .login import login  # noqa: E402
from .logout import logout  # noqa: E402
from .register import register  # noqa: E402
