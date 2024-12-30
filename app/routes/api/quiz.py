'''
app/routes/api/quiz.py

This module defines the API route for retrieving a specific quiz's details
along with its questions.

Routes:
    /api/quiz/<int:quiz_id>: Fetches and returns the details of a quiz
    along with its questions as a JSON response.
'''

from . import api_bp
from app.models import Quiz
from flask import jsonify


@api_bp.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):
    '''
    Fetches and returns the details of a specific quiz along
    with its questions.

    This route retrieves a quiz by its ID from the database. If the quiz
    does not exist,
    it raises a 404 error. The quiz details, including the list of questions,
    are returned as a JSON response.

    Args:
        quiz_id (int): The unique identifier of the quiz.

    Returns:
        Response: A JSON object containing the quiz details:
            - id (int): The ID of the quiz.
            - title (str): The title of the quiz.
            - description (str): The description of the quiz.
            - questions (list): A list of questions associated
            with the quiz, each containing:
                - id (int): The ID of the question.
                - text (str): The text of the question.
                - option_a (str): Option A for the question.
                - option_b (str): Option B for the question.
                - option_c (str): Option C for the question.
                - option_d (str): Option D for the question.
                - correct_option (str): The correct option
                ('a', 'b', 'c', or 'd').
    '''

    quiz = Quiz.query.get_or_404(quiz_id)
    quiz_data = {
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
    return jsonify(quiz_data)
