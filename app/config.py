'''
app/config.py

This module defines configuration classes for the Flask application.

Classes:
    Config: Base configuration class with common settings.
    ProductionConfig: Configuration for the production environment.
    DevelopmentConfig: Configuration for the development environment.
    TestingConfig: Configuration for the testing environment.

Attributes:
    SECRET_KEY (str): Secret key used by Flask for security features
    like sessions.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to disable tracking
    modifications in SQLAlchemy.
    SQLALCHEMY_DATABASE_URI (str): URI for the SQLAlchemy database.
    DEBUG (bool): Flag to enable/disable debug mode.
    TESTING (bool): Flag to enable/disable testing mode.
'''


class Config:
    '''
    Base configuration class with common settings for the application.

    Attributes:
        SECRET_KEY (str): Secret key used by Flask for security features
        like sessions.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to disable tracking
        modifications in SQLAlchemy.
    '''

    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    '''
    Configuration for the production environment.

    Inherits from Config and sets the appropriate database URI for production.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI for the production
        SQLAlchemy database.
    '''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///quizitnow.db'


class DevelopmentConfig(Config):
    '''
    Configuration for the development environment.

    Inherits from Config and sets the appropriate database URI for
    development and enables debug mode.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI for the development
        SQLAlchemy database.
        DEBUG (bool): Flag to enable debug mode in development.
    '''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///quizitnow_development.db'
    DEBUG = True


class TestingConfig(Config):
    '''
    Configuration for the testing environment.

    Inherits from Config and sets the database URI to use an in-memory
    database for testing purposes.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI for an in-memory SQLite
        database for testing.
        TESTING (bool): Flag to enable testing mode.
        DEBUG (bool): Flag to enable debug mode for testing.
    '''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = True
