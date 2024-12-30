'''
app/routes/home/main.py

This module defines the route for rendering the main page of the home section.

Routes:
    /: Renders the main home page template.
'''

from . import home_bp
from flask import render_template


@home_bp.route('/')
def main():
    '''
    Renders the main home page.

    This route renders the main page of the home section by rendering the
    `home/main.html` template.

    Returns:
        Response: The rendered HTML page for the home section.
    '''

    return render_template('home/main.html')
