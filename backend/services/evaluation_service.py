from typing import Dict, Any
from ..agents.answer_evaluator import AnswerEvaluator
from ..utils.excel_knowledge import get_question_data

class EvaluationService:
    """
    Coordinates the evaluation process by using the AnswerEvaluator agent.
    """
    def __init__(self):
        self.answer_evaluator = AnswerEvaluator()

    def evaluate_answer(self, question_id: str, user_answer: str) -> Dict[str, Any]:
        question_data = get_question_data(question_id)
        if not question_data:
            return {"error": "Question not found."}

        input_data = {
            "question": question_data["text"],
            "user_answer": user_answer,
            "correct_answer": question_data["correctAnswer"],
            "common_wrong_answers": question_data["commonWrongAnswers"],
            "evaluation_criteria": question_data["evaluationCriteria"],
        }
        
        return self.answer_evaluator.run(input_data)
