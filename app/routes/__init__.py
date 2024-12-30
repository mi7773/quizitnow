'''
app/routes/__init__.py

This module imports all the blueprints for different
sections of the application.
Each section (e.g., quizzes, dashboard, authentication, etc.)
is organized in its own module,
and its corresponding blueprint is imported here.
'''

# Importing the blueprints for each section of the app
from .quizzes import quizzes_bp
from .dashboard import dashboard_bp
from .admin import admin_bp
from .auth import auth_bp
from .profile import profile_bp
from .api import api_bp
from .home import home_bp
