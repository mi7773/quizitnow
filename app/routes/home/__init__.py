'''
app/routes/home/__init__.py

This module initializes the home blueprint for the Flask application.

Blueprint:
    home_bp: The blueprint for the home routes, responsible
    for rendering the main page.
'''

from flask import Blueprint

home_bp = Blueprint('home', __name__)

from .main import main  # noqa: E402
