'''
app/routes/auth/logout.py

This module defines the route for logging out a user.

Routes:
    /logout: Logs out the currently authenticated user
    and redirects to the home page.
'''

from . import auth_bp
from flask_login import current_user, logout_user
from flask import flash, redirect, url_for


@auth_bp.route('/logout')
def logout():
    '''
    Logs out the current user and redirects to the home page.

    This route logs out the authenticated user by calling the
    `logout_user()` function. If the user is not
    authenticated, a message is flashed, and the user is redirected
    to the home page.

    Returns:
        Response: A redirect to the home page after logging out or if the user
        is not authenticated.
    '''

    if not current_user.is_authenticated:
        flash('You are not logged in.', 'info')
        return redirect(url_for('home.main'))

    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home.main'))
