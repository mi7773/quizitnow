'''
app/routes/profile/edit.py

This module defines the route for editing the user profile.

Routes:
    /edit: Handles both GET and POST requests for editing
    the user's profile information.
'''

from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required
from .update_info import update_info
from . import profile_bp


@profile_bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    '''
    Handles the profile edit form submission and rendering.

    This route handles both the GET and POST requests for the profile
    edit page. On a POST request, it updates the 
    user's profile information. If the update is successful,
    a success message is flashed. If there are errors (e.g., 
    username or email already in use), an error message is flashed.

    Returns:
        Response: The rendered HTML page for editing the user profile,
        or a redirect upon successful form submission.
    '''

    if request.method == 'POST':
        check = update_info()

        if check == 'correct':
            flash('Changes saved!', 'success')
        elif check == 'used_username':
            flash('Username already exists.', 'danger')
        elif check == 'used_email':
            flash('Email already exists.', 'danger')

        return redirect(url_for('profile.edit'))

    return render_template('profile/edit.html')
