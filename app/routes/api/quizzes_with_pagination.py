'''
app/routes/api/quizzes_with_pagination.py

This module defines the function to fetch quizzes with pagination.

Function:
    quizzes_with_pagination: Retrieves a paginated list of quizzes with
    their details, including associated questions.

Args:
    page (int): The page number for pagination.
    per_page (int): The number of quizzes per page for pagination.

Returns:
    Response: A JSON response containing the list of quizzes, total count,
    total pages, and the current page.
'''

from app.models import Quiz
from flask import jsonify


def quizzes_with_pagination(page, per_page):
    '''
    Retrieves a paginated list of quizzes with their details.

    This function queries the database to get a page of quizzes.
    Each quiz includes its ID, title, description,
    and associated questions. The response also includes pagination
    information such as total quizzes, total pages,
    and the current page number.

    Args:
        page (int): The page number for pagination.
        per_page (int): The number of quizzes per page.

    Returns:
        Response: A JSON response containing the following information:
            - quizzes (list): A list of quizzes, each containing:
                - id (int): The ID of the quiz.
                - title (str): The title of the quiz.
                - description (str): The description of the quiz.
                - questions (list): A list of questions for the quiz,
                each containing:
                    - id (int): The ID of the question.
                    - text (str): The text of the question.
                    - option_a (str): Option A for the question.
                    - option_b (str): Option B for the question.
                    - option_c (str): Option C for the question.
                    - option_d (str): Option D for the question.
                    - correct_option (str): The correct option
                    ('a', 'b', 'c', or 'd').
            - total (int): The total number of quizzes available.
            - pages (int): The total number of pages for pagination.
            - current_page (int): The current page number.
    '''

    quizzes = Quiz.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
            )
    quizzes_data = [
            {
                'id': quiz.id,
                'title': quiz.title,
                'description': quiz.description,
                'questions': [
                    {
                        'id': question.id,
                        'text': question.text,
                        'option_a': question.option_a,
                        'option_b': question.option_b,
                        'option_c': question.option_c,
                        'option_d': question.option_d,
                        'correct_option': question.correct_option,
                        }
                    for question in quiz.questions
                    ]
                }
            for quiz in quizzes
            ]
    return jsonify({
        'quizzes': quizzes_data,
        'total': quizzes.total,
        'pages': quizzes.pages,
        'current_page': quizzes.page
        })
