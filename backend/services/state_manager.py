# This simple state manager uses in-memory storage for simplicity
# In a production environment, this would be backed by a database like Redis.
from typing import Dict, Any
import uuid

# In-memory storage for session state
_session_store: Dict[str, Dict[str, Any]] = {}

def create_session() -> str:
    """Creates a new session and returns its ID."""
    session_id = str(uuid.uuid4())
    _session_store[session_id] = {
        "evaluations": [],
        "current_question_id": None
    }
    return session_id

def get_session_state(session_id: str) -> Dict[str, Any]:
    """Retrieves the state for a given session ID."""
    return _session_store.get(session_id, {})

def update_session_state(session_id: str, key: str, value: Any):
    """Updates a key-value pair in a session's state."""
    if session_id in _session_store:
        _session_store[session_id][key] = value

def append_evaluation(session_id: str, evaluation: Dict[str, Any]):
    """Appends a new evaluation to the session's list of evaluations."""
    if session_id in _session_store:
        _session_store[session_id]["evaluations"].append(evaluation)
