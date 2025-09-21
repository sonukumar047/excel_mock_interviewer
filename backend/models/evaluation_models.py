from pydantic import BaseModel
from typing import List, Dict, Any

class EvaluationRequest(BaseModel):
    question_id: str
    user_answer: str
    session_id: str

class EvaluationResponse(BaseModel):
    score: int
    reasoning: str
