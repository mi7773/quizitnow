'''
app/routes/profile/update_info.py

This module defines the function to update the user's profile information.

Function:
    update_info: Validates and updates the user's profile details,
    such as name, username, and email.

Returns:
    str: A status message indicating the result of the update operation:
        - 'correct' if the update was successful,
        - 'used_username' if the provided username is already in use,
        - 'used_email' if the provided email is already in use.
'''

from flask import request
from flask_login import current_user
from app.extensions import db
from app.models import User


def update_info():
    '''
    Validates and updates the user's profile information.

    This function checks if the new username or email is already in use
    by other users. If valid, it updates the
    current user's name, username, and email in the database.

    Args:
        None

    Returns:
        str: A status message:
            - 'correct': If the update is successful.
            - 'used_username': If the username is already in use
            by another user.
            - 'used_email': If the email is already in use by another user.
    '''

    name = request.form['first_name']
    username = request.form['username']
    email = request.form['email']

    existing_user_name = User.query.filter_by(username=username).first()
    existing_user_email = User.query.filter_by(email=email).first()
    if existing_user_name:
        if existing_user_name.username != current_user.username:
            return 'used_username'
    if existing_user_email:
        if existing_user_email.email != current_user.email:
            return 'used_email'
    current_user.name = name
    current_user.username = username
    current_user.email = email

    db.session.commit()
    return 'correct'
