from fastapi import APIRouter, HTTPException
from ..models.interview_models import QuestionResponse
from ..agents.interview_manager import InterviewManager
from ..utils.excel_knowledge import EXCEL_QUESTIONS
from ..services import state_manager

router = APIRouter()

@router.post("/start", response_model=QuestionResponse)
async def start_interview():
    """Starts a new interview session and returns the first question."""
    session_id = state_manager.create_session()
    first_question = EXCEL_QUESTIONS[0]
    state_manager.update_session_state(session_id, "current_question_id", first_question["id"])
    return {
        "question": "Hello, I am the AI Excel Interviewer. I will be conducting your technical assessment today. We will go through a series of questions. Your answers will be evaluated on correctness and efficiency. Let's begin.",
        "question_id": first_question["id"],
        "is_last_question": len(EXCEL_QUESTIONS) == 1,
        "session_id": session_id
    }

@router.get("/next-question/{session_id}", response_model=QuestionResponse)
async def get_next_question(session_id: str):
    """Returns the next question in the interview sequence."""
    session_state = state_manager.get_session_state(session_id)
    if not session_state:
        raise HTTPException(status_code=404, detail="Session not found.")
        
    current_question_id = session_state.get("current_question_id")
    interview_manager = InterviewManager()
    
    # Find the next question based on the current one
    current_index = next((i for i, q in enumerate(EXCEL_QUESTIONS) if q["id"] == current_question_id), -1)
    
    if current_index + 1 >= len(EXCEL_QUESTIONS):
        return {
            "question": "End of interview. Please proceed to generate the report.",
            "question_id": "end",
            "is_last_question": True,
        }

    next_question = EXCEL_QUESTIONS[current_index + 1]
    state_manager.update_session_state(session_id, "current_question_id", next_question["id"])

    return {
        "question": next_question["text"],
        "question_id": next_question["id"],
        "is_last_question": (current_index + 2) == len(EXCEL_QUESTIONS),
    }
