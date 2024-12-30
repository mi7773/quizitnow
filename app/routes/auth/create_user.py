'''
app/routes/auth/create_user.py

This module defines the function to create a new user in the application.

Function:
    create_user: Validates user input and creates a new user in the database
    if the username and email are unique.

Returns:
    User or bool: A new `User` object if the creation is successful,
    or `False` if the username or email already exists.
'''

from flask import request
from werkzeug.security import generate_password_hash
from app.models import User
from app.extensions import db


def create_user():
    '''
    Validates user input and creates a new user if the username
    and email are unique.

    This function checks if the provided username or email is already in use
    by another user. If both are unique,
    it creates a new user, hashes the password, and saves the user
    to the database.

    Args:
        None

    Returns:
        User or bool:
            - `User`: A new `User` object if the creation is successful.
            - `False`: If the username or email is already taken.
    '''

    name = request.form['first_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(
            password,
            method='pbkdf2:sha256'
            )

    existing_user_name = User.query.filter_by(username=username).first()
    existing_user_email = User.query.filter_by(email=email).first()
    if existing_user_name or existing_user_email:
        return False

    new_user = User(
            name=name,
            username=username,
            password=hashed_password,
            email=email)
    db.session.add(new_user)
    db.session.commit()

    return new_user
