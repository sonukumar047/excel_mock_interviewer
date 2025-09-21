from fastapi import APIRouter
from pydantic import BaseModel
from ..services.state_manager import create_session

router = APIRouter()

class SessionResponse(BaseModel):
    session_id: str

@router.post("/create", response_model=SessionResponse)
async def create_new_session():
    """Creates a new interview session."""
    session_id = create_session()
    return {"session_id": session_id}
