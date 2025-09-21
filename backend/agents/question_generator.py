# This agent is not strictly necessary with the current design, as questions
# are pre-defined. However, it's included to match the modular structure
# and could be used for dynamic question generation in a future version.

from typing import Dict, Any
from .base_agent import BaseAgent
from ..utils.excel_knowledge import EXCEL_QUESTIONS

class QuestionGenerator(BaseAgent):
    """
    Generates or retrieves interview questions.
    """
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        question_id = input_data.get("question_id")
        if question_id:
            question = next((q for q in EXCEL_QUESTIONS if q["id"] == question_id), None)
            if question:
                return {"question": question}
        return {"error": "Question not found."}
