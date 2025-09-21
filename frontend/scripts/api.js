import { removeTypingIndicator } from './components.js';

// Base URL for the FastAPI backend
const BASE_URL = 'http://127.0.0.1:8000';

// A helper function to handle API responses and errors
async function handleResponse(response) {
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({ message: 'Unknown error occurred.' }));
        throw new Error(`HTTP Error: ${response.status} - ${errorData.detail || errorData.message}`);
    }
    return response.json();
}

/**
 * Creates a new interview session.
 * @returns {Promise<object>} The session object with a session_id.
 */
export async function createSession() {
    try {
        const response = await fetch(`${BASE_URL}/api/session/create`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });
        return handleResponse(response);
    } catch (error) {
        console.error('API Error in createSession:', error);
        throw error;
    }
}

/**
 * Gets the next question for the interview.
 * @param {string} sessionId The current session ID.
 * @returns {Promise<object>} The next question data.
 */
export async function getNextQuestion(sessionId) {
    try {
        const response = await fetch(`${BASE_URL}/api/interview/next-question/${sessionId}`, {
            method: 'GET',
        });
        return handleResponse(response);
    } catch (error) {
        console.error('API Error in getNextQuestion:', error);
        throw error;
    }
}

/**
 * Submits the user's answer for evaluation.
 * @param {string} sessionId The current session ID.
 * @param {string} questionId The ID of the current question.
 * @param {string} answer The user's answer.
 * @returns {Promise<object>} The evaluation result.
 */
export async function evaluateAnswer(sessionId, questionId, answer) {
    try {
        const response = await fetch(`${BASE_URL}/api/evaluation/evaluate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                session_id: sessionId,
                question_id: questionId,
                user_answer: answer
            }),
        });
        return handleResponse(response);
    } catch (error) {
        console.error('API Error in evaluateAnswer:', error);
        throw error;
    } finally {
        removeTypingIndicator();
    }
}

/**
 * Generates the final performance report.
 * @param {string} sessionId The current session ID.
 * @returns {Promise<object>} The final report data.
 */
export async function generateReport(sessionId) {
    try {
        const response = await fetch(`${BASE_URL}/api/evaluation/generate-report`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: sessionId }),
        });
        return handleResponse(response);
    } catch (error) {
        console.error('API Error in generateReport:', error);
        throw error;
    }
}
