from groq import Groq
from typing import Optional

_groq_client: Optional[Groq] = None

def get_groq_client(api_key: Optional[str] = None) -> Groq:
    """Initializes and returns a singleton Groq client."""
    global _groq_client
    if _groq_client is None:
        if not api_key:
            raise ValueError("API key must be provided to initialize the Groq client.")
        _groq_client = Groq(api_key=api_key)
    return _groq_client
