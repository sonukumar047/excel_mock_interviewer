import json
from typing import Dict, Any
from .base_agent import BaseAgent
from ..services.groq_service import get_groq_client
from ..config.settings import settings

class AnswerEvaluator(BaseAgent):
    """
    Evaluates a candidate's answer using the LLM.
    """
    def __init__(self):
        self.groq_client = get_groq_client()

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        question = input_data.get("question")
        user_answer = input_data.get("user_answer")
        correct_answer = input_data.get("correct_answer")
        common_wrong_answers = input_data.get("common_wrong_answers")
        evaluation_criteria = input_data.get("evaluation_criteria")

        evaluation_prompt = f"""
            You are a senior technical interviewer for Excel. Your task is to evaluate a candidate's answer to an Excel question.
            Instructions:
            1. Provide a score from 0 to 100, where 100 is a perfect answer.
            2. Provide a brief, professional explanation for the score.
            3. The output MUST be a valid JSON object with the keys "score" and "reasoning".
            Question: "{question}"
            Correct Answer: "{correct_answer}"
            Candidate's Answer: "{user_answer}"
            Common Incorrect Answers: "{', '.join(common_wrong_answers)}"
            Evaluation Criteria: "{evaluation_criteria}"
        """

        chat_completion = self.groq_client.chat.completions.create(
            messages=[{"role": "user", "content": evaluation_prompt}],
            model=settings.LLM_MODEL,
        )
        # Assuming the LLM returns a JSON string, which we will parse
        evaluation_string = chat_completion.choices[0].message.content
        try:
            return json.loads(evaluation_string)
        except json.JSONDecodeError:
            # Fallback for LLMs that don't strictly adhere to JSON
            return {"score": 50, "reasoning": "Could not parse LLM response."}
