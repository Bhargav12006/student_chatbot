from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_instance
import logging

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    """Render the main chat interface"""
    topics = chatbot_instance.get_help_topics()
    return render_template('index.html', topics=topics)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return bot response"""
    try:
        # Get user message from request
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'Please enter a message.', 'status': 'error'})
        
        # Log user message
        logger.info(f"User: {user_message}")
        
        # Get bot response
        bot_response = chatbot_instance.get_response(user_message)
        
        # Log bot response
        logger.info(f"Bot: {bot_response}")
        
        return jsonify({'response': bot_response, 'status': 'success'})
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return jsonify({'response': 'Sorry, an error occurred. Please try again.', 'status': 'error'})

@app.route('/clear', methods=['POST'])
def clear_session():
    """Clear chat history (just returns success)"""
    return jsonify({'status': 'success', 'message': 'Chat cleared'})

@app.route('/topics', methods=['GET'])
def get_topics():
    """Get list of topics the chatbot can help with"""
    topics = chatbot_instance.get_help_topics()
    return jsonify({'topics': topics})

if __name__ == '__main__':
    print("=" * 50)
    print("Student Support Chatbot Starting...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)