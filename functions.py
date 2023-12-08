import csv
import os
from typing import List, Union


def calculate_score(responses: List[int]) -> int:
    """
    Calculates the user's total score based on quiz responses, then returns it.
    """
    summation = 0
    for i in responses:
        summation += i
    return summation


def calculate_result(score: int) -> Union[str, None]:
    """
    Calculates the final result of the quiz based on the user's score.
    The range of point values must be from 10-50, based on the quiz's input.
    """
    if 10 <= score <= 17:
        return "Very violent"
    elif 18 <= score <= 25:
        return "Violent"
    elif 26 <= score <= 34:
        return "Neutral"
    elif 35 <= score <= 42:
        return "Peaceful"
    elif 43 <= score <= 50:
        return "Very peaceful"


def record_quiz(name: str, score: int, result: str) -> None:
    """
    Saves the gathered info to a CSV file.
    Creates a new file if one doesn't exist, with a proper header.
    """
    with open('quiz.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if os.path.exists('quiz.csv') and os.path.getsize('quiz.csv') == 0:
            writer.writerow(["Name", "Score", "Result"])
        writer.writerow([name, score, result])
