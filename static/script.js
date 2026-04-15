//Client-side chat functionality

class StudentChatbot {
    constructor() {
        this.chatContainer = document.getElementById('chatContainer');
        this.userInput = document.getElementById('userInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.clearBtn = document.getElementById('clearChatBtn');
        this.isLoading = false;
        
        this.initEventListeners();
    }
    
    initEventListeners() {
        // Send button click
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        
        // Enter key to send (Shift+Enter for new line)
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Auto-resize textarea
        this.userInput.addEventListener('input', () => {
            this.userInput.style.height = 'auto';
            this.userInput.style.height = Math.min(this.userInput.scrollHeight, 100) + 'px';
        });
        
        // Clear chat button
        this.clearBtn.addEventListener('click', () => this.clearChat());
        
        // Quick topic buttons
        document.querySelectorAll('.topic-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const topic = btn.getAttribute('data-topic');
                this.userInput.value = `Tell me about ${topic}`;
                this.sendMessage();
            });
        });
    }
    
    async sendMessage() {
        if (this.isLoading) return;
        
        const message = this.userInput.value.trim();
        if (!message) return;
        
        // Clear input
        this.userInput.value = '';
        this.userInput.style.height = 'auto';
        
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Show typing indicator
        this.showTypingIndicator();
        this.isLoading = true;
        
        try {
            // Send to backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Remove typing indicator
            this.removeTypingIndicator();
            
            // Add bot response
            this.addMessage(data.response, 'bot');
            
        } catch (error) {
            console.error('Error:', error);
            this.removeTypingIndicator();
            this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        } finally {
            this.isLoading = false;
            this.scrollToBottom();
        }
    }
    
    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const icon = sender === 'user' ? '👤' : '🤖';
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-icon">${icon}</div>
                <div class="message-text">${this.escapeHtml(text)}</div>
            </div>
        `;
        
        this.chatContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        typingDiv.id = 'typingIndicator';
        typingDiv.innerHTML = `
            <div class="message-content">
                <div class="message-icon">🤖</div>
                <div class="message-text">
                    <div class="typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </div>
        `;
        this.chatContainer.appendChild(typingDiv);
        this.scrollToBottom();
    }
    
    removeTypingIndicator() {
        const indicator = document.getElementById('typingIndicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    async clearChat() {
        try {
            await fetch('/clear', { method: 'POST' });
            
            // Clear chat container but keep welcome message
            while (this.chatContainer.firstChild) {
                this.chatContainer.removeChild(this.chatContainer.firstChild);
            }
            
            // Add welcome message back
            this.addMessage(
                "Hello! I'm your Student Support Assistant. 👋\n\nI can help you with:\n• Course information\n• Admission process\n• Fee structure\n• Class schedules\n• Exams and more!\n\nHow can I help you today?",
                'bot'
            );
            
        } catch (error) {
            console.error('Error clearing chat:', error);
        }
    }
    
    scrollToBottom() {
        this.chatContainer.scrollTop = this.chatContainer.scrollHeight;
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML.replace(/\n/g, '<br>');
    }
}

// Initialize chatbot when page loads
document.addEventListener('DOMContentLoaded', () => {
    new StudentChatbot();
});