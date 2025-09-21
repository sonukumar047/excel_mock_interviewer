from pydantic import BaseModel
from typing import List, Dict, Any

class QuestionResponse(BaseModel):
    question: str
    question_id: str
    is_last_question: bool

class InterviewState(BaseModel):
    session_id: str
    current_question_id: str
    evaluations: List[Dict[str, Any]] = []

class AnswerSubmission(BaseModel):
    session_id: str
    question_id: str
    user_answer: str

class ReportRequest(BaseModel):
    session_id: str
