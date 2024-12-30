'''
app/routes/api/quizzes.py

This module defines the API route for retrieving quizzes,
with support for pagination.

Routes:
    /api/quizzes: Fetches and returns the list of quizzes.
    Supports pagination if `page` and `per_page` query parameters are provided.
'''

from . import api_bp
from .quizzes_with_pagination import quizzes_with_pagination
from .quizzes_without_pagination import quizzes_without_pagination
from flask import request


@api_bp.route('/quizzes')
def quizzes():
    '''
    Fetches and returns the list of quizzes, with optional pagination.

    If the query parameters `page` and `per_page` are provided,
    the quizzes will be paginated.
    Otherwise, all quizzes are returned without pagination.

    Query Parameters:
        page (int, optional): The page number for pagination.
        per_page (int, optional): The number of quizzes
        per page for pagination.

    Returns:
        Response: A JSON response containing the list of quizzes.
        The format depends on whether pagination is used.
    '''

    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)

    if page is not None and per_page is not None:
        quizzes = quizzes_with_pagination(page, per_page)
    else:
        quizzes = quizzes_without_pagination()
    return quizzes
