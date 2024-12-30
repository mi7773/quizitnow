'''
app/routes/auth/check_user.py

This module defines the function to validate user credentials during login.

Function:
    check_user: Validates the provided username and password
    against the records in the database.

Returns:
    User or bool: A `User` object if the credentials are valid,
    or `False` if the username or password is incorrect.
'''

from app.models import User
from flask import request
from werkzeug.security import check_password_hash


def check_user():
    '''
    Validates the provided username and password.

    This function checks whether the given username exists in the database
    and if the provided password matches
    the stored hashed password for that user.

    Args:
        None

    Returns:
        User or bool:
            - `User`: The authenticated `User` object if the credentials
            are correct.
            - `False`: If the username does not exist
            or the password is incorrect.
    '''

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return False

    return user
