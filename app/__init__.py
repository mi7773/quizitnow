'''
app/__init__.py

This module defines the `create_app` function to initialize
and configure the Flask application.

Functions:
    create_app: Creates and configures the Flask application instance,
    setting up extensions and blueprints.

It also initializes the following components:
    - db: SQLAlchemy database extension.
    - login_manager: Flask-Login manager for user session handling.
    - Error handlers: Custom error handlers registered for the application.

Blueprints registered:
    - auth_bp: Blueprint for authentication routes.
    - dashboard_bp: Blueprint for user dashboard routes.
    - admin_bp: Blueprint for admin routes.
    - profile_bp: Blueprint for user profile routes.
    - quizzes_bp: Blueprint for quiz-related routes.
    - home_bp: Blueprint for home page routes.
    - api_bp: Blueprint for API routes.
'''

from flask import Flask
from .extensions import db, login_manager
from .error_handlers import register_error_handlers


def create_app(config_class):
    '''
    Creates and configures the Flask application instance.

    This function initializes the app with configurations
    from the specified config class,
    sets up the database, login manager, error handlers,
    and registers the blueprints.

    Args:
        config_class (str): The configuration class to load settings from.

    Returns:
        Flask: The initialized Flask application instance.
    '''

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import (
            auth_bp,
            dashboard_bp,
            admin_bp,
            profile_bp,
            quizzes_bp,
            home_bp,
            api_bp
            )
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(home_bp)

    register_error_handlers(app)

    return app
