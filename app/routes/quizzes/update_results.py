'''
app/routes/quizzes/update_results.py

This module contains the function to update the quiz results for a user.

Functions:
    update_results: Calculates the user's score and percentage for a quiz,
    and updates or creates a new quiz result.
'''

from app.extensions import db
from app.models import QuizResult
from flask_login import current_user
from flask import request


def update_results(quiz_id, quiz):
    '''
    Calculates the quiz score and updates the quiz result for the current user.

    This function compares the selected answers with the correct options
    for each question in the quiz.
    It then updates or creates a `QuizResult` record,
    storing the user's score and percentage.

    Args:
        quiz_id (int): The ID of the quiz.
        quiz (Quiz): The `Quiz` object containing questions
        and correct answers.

    Returns:
        int: The total score of the user for the quiz.
    '''

    score = 0
    for question in quiz.questions:
        selected_option_id = request.form.get(str(question.id))
        if selected_option_id:
            if selected_option_id.lower() == question.correct_option:
                score += 1
    percent = round(score / len(quiz.questions) * 100, 2)
    old_result = QuizResult.query.filter_by(
            quiz=quiz,
            user=current_user
            ).first()
    if old_result:
        old_result.score = score
        old_result.percent = percent
    else:
        result = QuizResult(
                user_id=current_user.id,
                quiz_id=quiz_id,
                score=score,
                percent=percent
                )
        db.session.add(result)
    db.session.commit()

    return score
