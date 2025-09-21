import json
from typing import Dict, Any, List
from .base_agent import BaseAgent
from ..services.groq_service import get_groq_client
from ..config.settings import settings

class FeedbackGenerator(BaseAgent):
    """
    Generates a final summary report based on interview evaluations.
    """
    def __init__(self):
        self.groq_client = get_groq_client()

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        evaluations: List[Dict[str, Any]] = input_data.get("evaluations", [])

        report_prompt = f"""
            You are a professional Excel interviewer. Generate a final interview report based on the following candidate evaluations. Provide a summary, highlight strengths and weaknesses, and give a final overall score (out of 100). The evaluations are a JSON array: {json.dumps(evaluations)}.
        """

        chat_completion = self.groq_client.chat.completions.create(
            messages=[{"role": "user", "content": report_prompt}],
            model=settings.LLM_MODEL,
        )
        report = chat_completion.choices[0].message.content
        return {"report": report}
