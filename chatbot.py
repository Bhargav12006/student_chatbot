#NLP processing for student chatbot
import nltk
import numpy as np
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

class StudentChatbot:
    def __init__(self):
        """Initialize the chatbot with training data"""
        self.intents = []
        self.patterns = []
        self.tags = []
        self.responses = {}
        self.vectorizer = TfidfVectorizer()
        self.is_trained = False
        
        # Load and prepare data
        self.load_data()
        
    def load_data(self):
        """Load intents from JSON file"""
        try:
            with open('data/responses.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.intents = data['intents']
            
            # Prepare training data
            self.patterns = []
            self.tags = []
            self.responses = {}
            
            for intent in self.intents:
                tag = intent['tag']
                self.responses[tag] = intent['responses']
                
                for pattern in intent['patterns']:
                    if pattern:  # Skip empty patterns
                        self.patterns.append(pattern.lower())
                        self.tags.append(tag)
            
            # Train the model
            self.train()
            
        except FileNotFoundError:
            print("Error: responses.json file not found!")
            # Create default responses
            self.create_default_responses()
        except json.JSONDecodeError:
            print("Error: Invalid JSON in responses.json!")
            self.create_default_responses()
    
    def create_default_responses(self):
        """Create default responses if JSON file is missing"""
        self.responses = {
            'greeting': ["Hello! How can I help you?"],
            'default': ["I'm here to help with student queries. Please ask about courses, admission, fees, or schedules."]
        }
        self.is_trained = False
    
    def train(self):
        """Train the TF-IDF vectorizer with patterns"""
        if len(self.patterns) > 0:
            try:
                self.vectorizer.fit(self.patterns)
                self.is_trained = True
                print(f"Chatbot trained successfully with {len(self.patterns)} patterns!")
            except Exception as e:
                print(f"Training error: {e}")
                self.is_trained = False
    
    def preprocess_text(self, text):
        """Clean and preprocess user input"""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters but keep letters, numbers, and spaces
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        # Remove extra spaces
        text = ' '.join(text.split())
        return text
    
    def get_response(self, user_input):
        """Get response for user input using similarity matching"""
        if not self.is_trained or len(self.patterns) == 0:
            return "I'm still learning! Please contact student support for immediate help."
        
        # Preprocess input
        processed_input = self.preprocess_text(user_input)
        
        if not processed_input:
            return "Please enter a valid question."
        
        try:
            # Transform input and patterns
            input_vector = self.vectorizer.transform([processed_input])
            patterns_vector = self.vectorizer.transform(self.patterns)
            
            # Calculate similarity
            similarities = cosine_similarity(input_vector, patterns_vector)
            max_similarity = np.max(similarities)
            max_index = np.argmax(similarities)
            
            # Set threshold for matching (0.2 is good for short queries)
            if max_similarity > 0.2:
                predicted_tag = self.tags[max_index]
                
                # Get random response for the tag
                import random
                responses_list = self.responses.get(predicted_tag, self.responses.get('fallback', 
                                                                  ["I'm not sure about that. Please contact support."]))
                response = random.choice(responses_list)
                return response
            else:
                # No good match found
                fallback_responses = self.responses.get('fallback', 
                                    ["I didn't understand. Could you please rephrase?"])
                import random
                return random.choice(fallback_responses)
                
        except Exception as e:
            print(f"Error getting response: {e}")
            return "Technical error. Please try again or contact support."
    
    def get_help_topics(self):
        """Return list of topics the chatbot can help with"""
        topics = []
        for intent in self.intents:
            if intent['tag'] not in ['greeting', 'bye', 'fallback']:
                topics.append(intent['tag'])
        return topics

# Create a single instance for the application
chatbot_instance = StudentChatbot()