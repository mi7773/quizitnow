'''
app/error_handlers.py

This module defines error handlers for the Flask application.

Functions:
    register_error_handlers: Registers custom error handlers
    for common HTTP errors (404, 500, 401, 403).
    cause_error: A test route to deliberately trigger
    a 500 internal server error for demonstration.

Error Handlers:
    404: Not Found error, rendered with a custom 404 template.
    500: Internal Server error, rendered with a custom 500 template.
    401: Unauthorized error, with a flash message redirecting
    to the register page.
    403: Forbidden error, rendered with a custom 403 template.
'''

from flask import render_template, flash, redirect, url_for, request, abort


def register_error_handlers(app):
    '''
    Registers custom error handlers for various HTTP errors.

    This function defines handlers for the following error codes:
        - 404 (Not Found)
        - 500 (Internal Server Error)
        - 401 (Unauthorized)
        - 403 (Forbidden)

    Args:
        app (Flask): The Flask application instance.

    '''

    @app.route('/cause_error')
    def cause_error():
        '''
        A test route that deliberately triggers a 500 internal server error.

        Returns:
            None: This route will cause an error to demonstrate
            the error handler in action.
        '''

        abort(500)

    @app.errorhandler(404)
    def not_found_error(error):
        '''
        Handles 404 Not Found errors.

        Args:
            error (Exception): The error object.

        Returns:
            tuple: A tuple containing the rendered template
            and HTTP status code 404.
        '''

        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        '''
        Handles 500 Internal Server errors.

        Args:
            error (Exception): The error object.

        Returns:
            tuple: A tuple containing the rendered template
            and HTTP status code 500.
        '''

        return render_template('error/500.html'), 500

    @app.errorhandler(401)
    def unauthorized_error(error):
        '''
        Handles 401 Unauthorized errors by flashing a message
        and redirecting the user to the registration page.

        Args:
            error (Exception): The error object.

        Returns:
            redirect: A redirect to the registration page with
            the original URL passed as the `next` argument.
        '''

        flash('You must register in to access this page.', 'info')
        return redirect(url_for('auth.register', next=request.url))

    @app.errorhandler(403)
    def forbidden_error(error):
        '''
        Handles 403 Forbidden errors.

        Args:
            error (Exception): The error object.

        Returns:
            tuple: A tuple containing the rendered template
            and HTTP status code 403.
        '''

        return render_template('error/403.html'), 403
