from typing import List, Dict, Any

# This is the single source of truth for all Excel questions.
EXCEL_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "q1",
        "text": "Let's start with a foundational question. Can you explain the difference between the `VLOOKUP` and `HLOOKUP` functions in Excel?",
        "correctAnswer": "VLOOKUP searches for a value in a column (vertically) and returns a corresponding value from the same row. HLOOKUP searches for a value in a row (horizontally) and returns a value from the same column.",
        "commonWrongAnswers": ["They do the same thing.", "VLOOKUP is faster.", "HLOOKUP is used for horizontal data, but doesn't explain the return value."],
        "evaluationCriteria": "Score based on mentioning the vertical (column) vs. horizontal (row) lookup and correctly explaining the return behavior."
    },
    {
        "id": "q2",
        "text": "Describe the purpose of the `IFERROR` function and provide a simple example of how you would use it.",
        "correctAnswer": "The IFERROR function checks if a formula results in an error. If it does, it returns a value you specify; otherwise, it returns the result of the formula. Example: `=IFERROR(VLOOKUP(A2, B:C, 2, FALSE), 'Not Found')`.",
        "commonWrongAnswers": ["It fixes all errors.", "It's only for VLOOKUP.", "It shows a pop-up error message."],
        "evaluationCriteria": "Score based on explaining its purpose (checking for errors) and providing a correct, formula-based example."
    },
    {
        "id": "q3",
        "text": "Imagine you have a large dataset of sales records. How would you quickly find the top 5 highest-selling products without manually sorting the entire list?",
        "correctAnswer": "You could use the `LARGE` function, a combination of `INDEX` and `MATCH`, or a PivotTable with a top-N filter.",
        "commonWrongAnswers": ["Manually sorting the data.", "Using the `MAX` function.", "Using a filter."],
        "evaluationCriteria": "Score based on mentioning functions like `LARGE`, `INDEX`/`MATCH`, or using a `PivotTable` for efficiency."
    },
    {
        "id": "q4",
        "text": "Explain the concept of an absolute reference in Excel and how you would create one for a cell like B2.",
        "correctAnswer": "An absolute reference locks a cell, preventing it from changing when a formula is copied to other cells. You create one by adding a dollar sign ($) before both the column and row, for example, `$B$2`.",
        "commonWrongAnswers": ["It's just a named cell.", "It's only for rows.", "It's for a whole range."],
        "evaluationCriteria": "Score based on a clear definition of an absolute reference and the correct syntax (`$B$2`)."
    },
    {
        "id": "q5",
        "text": "What is a PivotTable and what is its primary use case in data analysis?",
        "correctAnswer": "A PivotTable is a powerful data summarization tool used to quickly calculate, summarize, and analyze data by rearranging it into a different view. Its primary use case is to easily identify patterns and trends in large datasets.",
        "commonWrongAnswers": ["It's a way to sort data.", "It's just another kind of chart.", "It's a complex formula."],
        "evaluationCriteria": "Score based on a definition that highlights its use for summarizing/aggregating large datasets for analysis."
    }
]

def get_question_data(question_id: str) -> Dict[str, Any]:
    """Retrieves question data by ID."""
    return next((q for q in EXCEL_QUESTIONS if q["id"] == question_id), None)
