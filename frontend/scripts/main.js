import { startInterview, handleUserAnswer } from './interview.js';

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');

    chatForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const userAnswer = userInput.value.trim();
        if (userAnswer) {
            handleUserAnswer(userAnswer);
            userInput.value = '';
        }
    });

    startInterview();
});
