from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

# Create the FastAPI application instance
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) middleware
# This is crucial for allowing the frontend running on a different port/origin to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development purposes. In production, you'd specify your frontend's domain.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Mock data for the interview.
# In a real application, this would be stored in a database or a file.
QUESTIONS = [
    {
        "question_id": "q1",
        "question": "Imagine you have a sales dataset with columns: 'Date', 'Product', 'Region', and 'Sales Amount'. What is the single Excel function you would use to calculate the total sales for 'Product B' in the 'North' region?",
    },
    {
        "question_id": "q2",
        "question": "You have a list of employee birthdays in column A and you want to highlight all employees with a birthday in the current month. How would you do this using conditional formatting?",
    },
    {
        "question_id": "q3",
        "question": "The VLOOKUP function is a classic, but it has limitations. What are some of the key disadvantages of VLOOKUP, and what is a more modern, flexible alternative you could use?",
    },
    {
        "question_id": "end",
        "question": "Thank you for completing the mock interview! Your final report is being generated...",
    },
]

# A simple in-memory session store for this example
sessions = {}


class UserAnswer(BaseModel):
    session_id: str
    question_id: str
    user_answer: str


class SessionCreateResponse(BaseModel):
    session_id: str


class NextQuestionResponse(BaseModel):
    question_id: str
    question: str
    is_last_question: bool = False


class EvaluationResponse(BaseModel):
    score: int
    reasoning: str


class ReportResponse(BaseModel):
    report: str


# Root endpoint to confirm the server is running
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


# Endpoint to create a new interview session
@app.post("/api/session/create", response_model=SessionCreateResponse)
async def create_session():
    session_id = str(int(time.time()))
    sessions[session_id] = {"question_index": 0}
    return {"session_id": session_id}


# Endpoint to get the next question in the interview sequence
@app.get("/api/interview/next-question/{session_id}", response_model=NextQuestionResponse)
async def get_next_question(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    session_data = sessions[session_id]
    question_index = session_data["question_index"]

    if question_index >= len(QUESTIONS):
        return NextQuestionResponse(
            question_id="end",
            question="Thank you for completing the interview! Your final report is being generated...",
            is_last_question=True
        )

    question_data = QUESTIONS[question_index]
    session_data["question_index"] += 1

    return NextQuestionResponse(
        question_id=question_data["question_id"],
        question=question_data["question"],
        is_last_question=(question_index == len(QUESTIONS) - 1)
    )


# Endpoint to evaluate the user's answer
# This endpoint currently returns a mock evaluation
@app.post("/api/evaluation/evaluate", response_model=EvaluationResponse)
async def evaluate_answer(user_answer: UserAnswer):
    # This is a mock evaluation. In a future step, this will call a Gemini API to evaluate the answer.
    score = 85
    reasoning = "Your answer was mostly correct, but it lacked detail on handling edge cases. Make sure to specify the exact syntax."
    return EvaluationResponse(score=score, reasoning=reasoning)


# Endpoint to generate the final report
# This endpoint currently returns a mock report
@app.post("/api/evaluation/generate-report", response_model=ReportResponse)
async def generate_report(request: Request):
    # This is a mock report. A future step will use the Gemini API to generate a comprehensive report.
    report_text = """
    **Final Interview Report**

    **Overall Score:** 85%

    **Strengths:**
    - Strong understanding of core Excel functions like SUMIF/SUMIFS.
    - Good grasp of conditional formatting principles.

    **Areas for Improvement:**
    - Need to be more specific with formula syntax and arguments.
    - Consider alternative solutions beyond the most common ones.

    **Next Steps:**
    - Practice with more complex nested functions and array formulas.
    - Explore the XLOOKUP function and its capabilities.
    """
    return ReportResponse(report=report_text)
