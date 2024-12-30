'''
app/routes/auth/login.py

This module defines the route for logging in a user.

Routes:
    /login: Handles the login process for users, including validation
    of credentials and redirection to the dashboard.

Functions:
    login: Manages user login by checking credentials,
    logging in the user, and handling redirection to the intended page.
'''

from . import auth_bp
from flask import request, flash, url_for, redirect, render_template
from flask_login import login_user, current_user
from .check_user import check_user


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Handles user login and redirection.

    If the user is already authenticated, they are redirected to the dashboard.
    If the user is not authenticated,
    their credentials are checked, and upon successful login,
    they are redirected to the intended page or dashboard.

    Args:
        None

    Returns:
        Response:
            - If the user is logged in, they are redirected to the dashboard.
            - If login fails, they are redirected to the login page
            with a flash message.
            - If login succeeds, they are redirected to the intended page
            or dashboard.
    '''

    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('dashboard.main'))

    if request.method == 'POST':
        user = check_user()

        if not user:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user)
        flash('Logged in successfully!', 'success')
        next_page = request.args.get('next')
        if not next_page or next_page.startswith('/auth'):
            next_page = url_for('dashboard.main')
        return redirect(next_page)

    return render_template('auth/login.html')
