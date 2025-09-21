from typing import Dict, Any
from .base_agent import BaseAgent
from ..utils.excel_knowledge import EXCEL_QUESTIONS

class InterviewManager(BaseAgent):
    """
    Manages the overall flow of the interview, including question sequencing
    and state transitions.
    """
    def __init__(self):
        self.questions = EXCEL_QUESTIONS
        self.current_question_index = 0

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Retrieves the next question in the sequence.
        """
        question_id = input_data.get("question_id")
        if question_id is None:
            # Return the first question
            question_data = self.questions[0]
            return {
                "question": question_data["text"],
                "question_id": question_data["id"],
                "is_last_question": len(self.questions) == 1
            }
        else:
            # Find the index of the next question
            current_index = next((i for i, q in enumerate(self.questions) if q["id"] == question_id), None)
            next_index = current_index + 1
            
            if next_index < len(self.questions):
                question_data = self.questions[next_index]
                return {
                    "question": question_data["text"],
                    "question_id": question_data["id"],
                    "is_last_question": next_index == len(self.questions) - 1
                }
            else:
                return {
                    "message": "End of interview. Please proceed to generate the report."
                }
