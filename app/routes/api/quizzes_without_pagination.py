'''
app/routes/api/quizzes_without_pagination.py

This module defines the function to fetch all quizzes without pagination.

Function:
    quizzes_without_pagination: Retrieves a list of all quizzes
    with their details, including associated questions.

Returns:
    Response: A JSON response containing the list of all quizzes
    and the total number of quizzes.
'''

from app.models import Quiz
from flask import jsonify


def quizzes_without_pagination():
    '''
    Retrieves a list of all quizzes with their details.

    This function queries the database to retrieve all quizzes.
    Each quiz includes its ID, title, description,
    and associated questions. The response includes the total number
    of quizzes.

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
            - total (int): The total number of quizzes.
    '''

    quizzes = Quiz.query.all()
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
        'total': len(quizzes_data)
        })
