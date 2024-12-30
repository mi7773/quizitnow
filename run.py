'''
run.py

This module serves as the entry point for running the Flask application.

It creates an application instance using the production configuration
and starts the server.

Usage:
    python run.py

Modules:
    create_app: Function to create and configure
    the Flask application instance.
    ProductionConfig: The configuration class for the production environment.
'''

from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
