const chatMessagesContainer = document.getElementById('chat-messages');

export function addAIMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('flex', 'justify-start', 'mb-4');
    messageElement.innerHTML = `
        <div class="bg-gray-200 text-gray-800 p-3 rounded-lg max-w-[80%] shadow-md">
            <div class="chat-message" style="display: none;">${message}</div>
        </div>
    `;
    chatMessagesContainer.appendChild(messageElement);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;

    const chatMessageDiv = messageElement.querySelector('.chat-message');
    // Simple typewriter effect
    let i = 0;
    const speed = 20; // Typing speed in milliseconds
    function typeWriter() {
        if (i < message.length) {
            chatMessageDiv.style.display = 'block';
            chatMessageDiv.textContent += message.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }
    typeWriter();
}

export function addUserMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('flex', 'justify-end', 'mb-4');
    messageElement.innerHTML = `
        <div class="bg-blue-500 text-white p-3 rounded-lg max-w-[80%] shadow-md">
            ${message}
        </div>
    `;
    chatMessagesContainer.appendChild(messageElement);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
}

export function addTypingIndicator() {
    const typingIndicator = document.createElement('div');
    typingIndicator.id = 'typing-indicator';
    typingIndicator.classList.add('flex', 'justify-start', 'mb-4');
    typingIndicator.innerHTML = `
        <div class="bg-gray-200 p-3 rounded-lg max-w-[80%] shadow-md">
            <div class="flex space-x-2">
                <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce"></div>
                <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style="animation-delay: 0.2s;"></div>
                <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style="animation-delay: 0.4s;"></div>
            </div>
        </div>
    `;
    chatMessagesContainer.appendChild(typingIndicator);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
}

export function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}
