
# 🤖 AI Student Chatbot

An **Intent-based Intelligent Chatbot** designed for students to answer academic questions instantly. Built with Python, NLTK, and JSON-based intent mapping. No internet required - works completely offline!

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![NLTK](https://img.shields.io/badge/NLTK-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 💬 **Intent-based Responses** | Predefined Q&A mapping using JSON intents |
| 📚 **Academic Focus** | Covers Programming, Math, Science, English, GK |
| 🔌 **Offline First** | Works completely without internet |
| 🧠 **NLP Powered** | Uses NLTK for text preprocessing & pattern matching |
| 📝 **Easy to Customize** | Add new Q&A by simply editing JSON file |
| 🖥️ **Terminal Interface** | Simple command-line chat interface |
| ⚡ **Fast Responses** | Instant answers with low latency |

---

## 📁 Project Structure
student_chatbot/
│
├── chatbot.py # Main chatbot engine
├── train_chatbot.py # Training script
├── intents.json # JSON file with Q&A patterns
├── words.pkl # Pickled words list (generated)
├── classes.pkl # Pickled classes list (generated)
├── chatbot_model.h5 # Trained Keras model
├── requirements.txt # Python dependencies
└── README.md # Documentation

text

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **NLTK** | Text preprocessing (tokenization, lemmatization, stopwords) |
| **TensorFlow/Keras** | Neural network for intent classification |
| **JSON** | Intent storage and management |
| **Pickle** | Serializing words and classes |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step 1: Clone the Repository
git clone https://github.com/Bharghav12006/student_chatbot.git
cd student_chatbot

###Step 2: Create Virtual Environment (Recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

###Step 3: Install Dependencies
pip install -r requirements.txt

###Step 4: Download NLTK Data
python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

###Step 5: Train the Chatbot
python train_chatbot.py
This will generate:
words.pkl
classes.pkl
chatbot_model.h5

###Step 6: Run the Chatbot
python chatbot.py
💬 How to Use
Starting the Chatbot:
python chatbot.py
Sample Conversation:
text
You: What is Python?
Bot: Python is a high-level, interpreted programming language known for its simplicity and readability.

You: Explain machine learning
Bot: Machine Learning is a subset of AI that allows systems to learn from data without being explicitly programmed.

You: What is photosynthesis?
Bot: Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into glucose and oxygen.

You: Tell me a noun example
Bot: A noun is a naming word. Examples: cat, Mumbai, John, book.

You: quit
Bot: Goodbye! Happy learning!

🎓 Built-in Academic Topics
Subject	Example Questions
Programming	What is Python? What is a variable? What is OOP?
Mathematics	What is Pythagoras theorem? What is algebra?
Science	What is photosynthesis? What is Newton's law?
English	What is a noun? What is a verb? What is tense?
General Knowledge	Who is the CEO of Microsoft? What is the capital of India?
Exam Tips	How to prepare for exams? Time management tips?
🔧 Customization Guide
How to Add New Questions & Answers:
Open intents.json file

python train_chatbot.py

📊 How It Works (Architecture)
text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  User Input │────▶│  Text Pre-  │────▶│  Tokenize & │
│  (Question) │     │  processing │     │  Lemmatize  │
└─────────────┘     └─────────────┘     └─────────────┘
                                                  │
                                                  ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Response   │◀────│  Predict    │◀────│  Bag of     │
│  Output     │     │  Intent     │     │  Words      │
└─────────────┘     └─────────────┘     └─────────────┘
Algorithm Steps:
Input - User types a question

Preprocessing - Tokenization, lemmatization, removing stopwords

Bag of Words - Convert text to numerical format

Prediction - Neural network predicts intent class

Response - Random response from matched intent's responses

📦 Dependencies (requirements.txt)
txt
nltk==3.8.1
tensorflow==2.13.0
numpy==1.24.3
pickle-mixin==1.0.2
❓ Troubleshooting
Issue: NLTK data not found
Solution:

python
import nltk
nltk.download('all')
Issue: TensorFlow/Keras import error
Solution:
pip uninstall tensorflow
pip install tensorflow==2.13.0
Issue: Model not training
Solution: Check if intents.json is properly formatted (valid JSON)

Issue: Chatbot giving wrong responses
Solution: Add more patterns to intents.json and retrain

🚧 Future Improvements
Add GUI using Tkinter or PyQt

Integrate with Flask for web interface

Add speech recognition (voice input)

Support for multiple languages (Hindi, etc.)

Add memory to remember conversation context

Deploy as WhatsApp or Telegram bot

Add image/document understanding capability

🤝 Contributing
Contributions are welcome!

Fork the repository

Create feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📧 Contact
Bhargav

GitHub: @Bhargav12006

Project Link: https://github.com/Bhargav12006/student_chatbot

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

⭐ Show Your Support
If this chatbot helped you or your studies, please give it a ⭐ on GitHub!

🙏 Acknowledgements
NLTK for text processing capabilities
TensorFlow for deep learning framework
All contributors and users
