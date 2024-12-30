'''
app/routes/auth/register.py

This module defines the route for user registration.

Routes:
    /register: Handles the user registration process,
    including validation of username/email uniqueness,
    user creation, and login.

Functions:
    register: Manages user registration by checking if the user
    is authenticated, processing the registration form,
    creating a new user, and redirecting to the dashboard.
'''

from . import auth_bp
from .create_user import create_user
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, current_user


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Handles user registration and login.

    If the user is already logged in, they are redirected to the dashboard.
    If the user is not authenticated,
    their registration details are checked, and upon successful registration,
    the user is logged in and redirected
    to the intended page or dashboard.

    Args:
        None

    Returns:
        Response:
            - If the user is logged in, they are redirected to the dashboard.
            - If registration fails (due to duplicate username or email),
            the user is redirected to the registration page
            with a flash message.
            - If registration succeeds, the user is logged in
            and redirected to the intended page or dashboard.
    '''

    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('dashboard.main'))

    if request.method == 'POST':
        new_user = create_user()

        if not new_user:
            flash('The username or email is already in use.', 'danger')
            return redirect(url_for('auth.register'))

        flash('Registration successful.', 'success')
        login_user(new_user)
        next_page = request.args.get('next')
        if not next_page or next_page.startswith('/auth'):
            next_page = url_for('dashboard.main')
        return redirect(next_page)

    return render_template('auth/register.html')
