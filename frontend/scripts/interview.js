import { createSession, getNextQuestion, evaluateAnswer, generateReport } from './api.js';
import { addAIMessage, addUserMessage, addTypingIndicator, removeTypingIndicator } from './components.js';

const sendButton = document.getElementById('send-button');
const userInput = document.getElementById('user-input');

let interviewState = {
    sessionId: null,
    currentQuestionId: null,
    isProcessing: false,
    isInterviewFinished: false,
};

// Disable input and button when processing
const toggleProcessing = (isProcessing) => {
    interviewState.isProcessing = isProcessing;
    sendButton.disabled = isProcessing;
    userInput.disabled = isProcessing;
    if (isProcessing) {
        addTypingIndicator();
    } else {
        removeTypingIndicator();
    }
};

export async function startInterview() {
    try {
        addTypingIndicator();
        const session = await createSession();
        interviewState.sessionId = session.session_id;

        removeTypingIndicator();
        addAIMessage("Hello, I am the AI Excel Interviewer. I will be conducting your technical assessment today. We will go through a series of questions. Your answers will be evaluated on correctness and efficiency. Let's begin. ");
        
        await new Promise(resolve => setTimeout(resolve, 2000));
        await askNextQuestion();

    } catch (error) {
        console.error("Failed to start interview:", error);
        removeTypingIndicator();
        addAIMessage("I'm sorry, I couldn't connect to the interview server. Please check the backend service. Error details are logged to the console.");
    }
}

export async function handleUserAnswer(userAnswer) {
    if (interviewState.isProcessing || interviewState.isInterviewFinished) {
        return;
    }

    addUserMessage(userAnswer);
    toggleProcessing(true);

    try {
        await evaluateAnswer(interviewState.sessionId, interviewState.currentQuestionId, userAnswer);
        await askNextQuestion();
    } catch (error) {
        console.error("Error during answer evaluation or next question fetch:", error);
        addAIMessage(`I'm sorry, an error occurred while processing your answer. Please check the browser console and the backend server logs for more details. Error: ${error.message}`);
        toggleProcessing(false);
    }
}

async function askNextQuestion() {
    toggleProcessing(true);
    try {
        const nextQuestionData = await getNextQuestion(interviewState.sessionId);
        toggleProcessing(false);

        if (nextQuestionData.is_last_question && nextQuestionData.question_id === 'end') {
            addAIMessage(nextQuestionData.question);
            interviewState.isInterviewFinished = true;
            await new Promise(resolve => setTimeout(resolve, 2000));
            await generateFinalReport();
        } else {
            addAIMessage(nextQuestionData.question);
            interviewState.currentQuestionId = nextQuestionData.question_id;
        }
    } catch (error) {
        console.error("Error fetching next question:", error);
        toggleProcessing(false);
        addAIMessage("I'm sorry, an error occurred while getting the next question. Please check the backend server and try again.");
    }
}

async function generateFinalReport() {
    toggleProcessing(true);
    try {
        const reportData = await generateReport(interviewState.sessionId);
        toggleProcessing(false);
        addAIMessage("Thank you for your time. Here is your final performance report:");
        addAIMessage(reportData.report);
    } catch (error) {
        console.error("Error generating report:", error);
        toggleProcessing(false);
        addAIMessage("I'm sorry, an error occurred while generating your report. Please try again later.");
    }
}
