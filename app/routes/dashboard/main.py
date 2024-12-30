'''
app/routes/dashboard/main.py

This module defines the route for the main dashboard page.
It is accessible only to logged-in users.

Routes:
    - main: Displays the main dashboard page for logged-in users.
'''

from . import dashboard_bp
from flask import render_template
from flask_login import login_required


@dashboard_bp.route('')
@login_required
def main():
    '''
    Renders the main dashboard page for logged-in users.

    The dashboard page is displayed only if the user is authenticated.

    Returns:
        render_template: The rendered main dashboard HTML page.
    '''

    return render_template('dashboard/main.html')
