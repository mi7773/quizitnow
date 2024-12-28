'''
app/extensions.py

This module initializes and provides extensions for the Flask application.

Extensions:
    db: An instance of SQLAlchemy used for database interactions.
    login_manager: An instance of LoginManager used for managing user sessions
    in Flask-Login.
'''

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
