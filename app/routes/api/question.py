'''
app/routes/api/question.py

This module defines the API route for retrieving a specific question's details.

Routes:
    /api/question/<int:question_id>: Fetches and returns the details
    of a question as a JSON response.
'''

from app.models import Question
from . import api_bp
from flask import jsonify


@api_bp.route('/question/<int:question_id>')
def question(question_id):
    '''
    Fetches and returns the details of a specific question.

    This route retrieves a question by its ID from the database.
    If the question does not exist,
    it raises a 404 error. The question details are returned
    as a JSON response.

    Args:
        question_id (int): The unique identifier of the question.

    Returns:
        Response: A JSON object containing the question details:
            - id (int): The ID of the question.
            - text (str): The question text.
            - option_a (str): Option A for the question.
            - option_b (str): Option B for the question.
            - option_c (str): Option C for the question.
            - option_d (str): Option D for the question.
            - correct_option (str): The correct option ('a', 'b', 'c', or 'd').
    '''

    question = Question.query.get_or_404(question_id)
    question_data = {
            'id': question.id,
            'text': question.text,
            'option_a': question.option_a,
            'option_b': question.option_b,
            'option_c': question.option_c,
            'option_d': question.option_d,
            'correct_option': question.correct_option,
            }
    return jsonify(question_data)
