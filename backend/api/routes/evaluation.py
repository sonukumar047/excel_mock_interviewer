from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from ..services.evaluation_service import EvaluationService
from ..services.state_manager import append_evaluation
from ..utils.excel_knowledge import get_question_data
from ..agents.feedback_generator import FeedbackGenerator

router = APIRouter()

class EvaluationRequest(BaseModel):
    session_id: str
    question_id: str
    user_answer: str

class ReportRequest(BaseModel):
    session_id: str

@router.post("/evaluate")
async def evaluate_answer(request: EvaluationRequest):
    """Evaluates a candidate's answer for a given question."""
    question_data = get_question_data(request.question_id)
    if not question_data:
        raise HTTPException(status_code=404, detail="Question not found.")
    
    eval_service = EvaluationService()
    evaluation_result = eval_service.evaluate_answer(request.question_id, request.user_answer)
    
    # Append the evaluation to the session state
    evaluation_data = {
        "question": question_data["text"],
        "answer": request.user_answer,
        "score": evaluation_result.get("score"),
        "reasoning": evaluation_result.get("reasoning"),
    }
    append_evaluation(request.session_id, evaluation_data)
    
    return evaluation_result

@router.post("/generate-report")
async def generate_report(request: ReportRequest):
    """Generates the final interview report."""
    from ..services.state_manager import get_session_state
    
    session_state = get_session_state(request.session_id)
    if not session_state:
        raise HTTPException(status_code=404, detail="Session not found.")
        
    feedback_generator = FeedbackGenerator()
    report_data = feedback_generator.run({"evaluations": session_state.get("evaluations", [])})
    
    return report_data
