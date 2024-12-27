'''
app/models/user.py

This module defines the User model for a Flask application
and the user loader for Flask-Login.

Classes:
    User: Represents a user in the system, with fields for username,
    email, password, and role.

Functions:
    load_user: Loads a user from the database by their user ID
    for session management in Flask-Login.

Attributes:
    id (int): Primary key for the user.
    username (str): Unique username of the user.
    name (str): The full name of the user.
    email (str): Unique email address of the user.
    password (str): The user's password (hashed).
    role (str): The user's role in the system (default is 'user').
'''

from app.extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    '''
    Represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Unique username of the user.
        name (str): Full name of the user.
        email (str): Email address of the user.
        password (str): Hashed password for the user.
        role (str): Role assigned to the user (default is 'user').
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')


@login_manager.user_loader
def load_user(user_id):
    '''
    Loads a user from the database by their user ID.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        User: The user object corresponding to the given user_id,
        or None if not found.
    '''

    return User.query.get(int(user_id))
