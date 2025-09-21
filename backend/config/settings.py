import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    API_URL: str = "https://api.groq.com/openai/v1"
    LLM_MODEL: str = "llama3-8b-8192"

settings = Settings()
