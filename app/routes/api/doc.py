'''
app/routes/api/doc.py

This module defines the API documentation route for the Flask application.

Routes:
    /api/doc: Serves the API documentation page. 
'''

from . import api_bp
from flask import render_template


@api_bp.route('/doc')
def doc():
    '''
    Renders the API documentation page.
    
    Returns:
        Response: The rendered HTML template for the API documentation.
    '''

    return render_template('api/doc.html')
