'''
create_db.py

This script is used to create the database tables for the application.
It initializes the application and creates the tables defined
in the database models.

Usage:
    python create_db.py

The script will:
    - Initialize the application with the production configuration.
    - Create all the tables defined in the database models.

Modules:
    app: The application module that contains the configuration
    and extension setup.
    app.config: The module that holds different configurations
    for the application.
    app.extensions: The module where the database extension is initialized.

Main Functions:
    __main__: Creates the database tables using the current app context.
'''

from app import create_app
from app.config import ProductionConfig
from app.extensions import db

if __name__ == '__main__':
    '''
    Main entry point of the script. Creates the database tables.

    This function:
        - Initializes the app using the ProductionConfig.
        - Uses the app context to create all tables defined
        in the app's database models.
    '''

    app = create_app(ProductionConfig)
    with app.app_context():
        db.create_all()
