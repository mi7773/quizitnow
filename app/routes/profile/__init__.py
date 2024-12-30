'''
app/routes/profile/__init__.py

This module initializes the profile blueprint for the Flask application.

Blueprint:
    profile_bp: The blueprint for the profile routes,
    responsible for rendering profile-related pages.
'''

from flask import Blueprint

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

from .edit import edit  # noqa: E402
