# Ai-Chatbot-Python
# 🤖 AI Chatbot using Python

A simple AI-powered chatbot built with Python that accepts user messages, sends them to an AI model through an API, receives the generated response, and displays it to the user.

This project was developed as part of my **AI Internship — Day 1 Practical Task** to demonstrate basic AI API integration, Python programming, environment variable management, and Git/GitHub workflow.

---

## 📌 Project Overview

The chatbot provides a simple interface for interacting with an AI model.

The basic workflow is:

```text
User
  ↓
Enter Message
  ↓
Python Chatbot
  ↓
AI API
  ↓
AI Model
  ↓
Generated Response
  ↓
Chatbot displays Response
```

The project focuses on understanding how an application communicates with an AI model through an API.

---

## ✨ Features

* 💬 Accepts user messages
* 🤖 Sends messages to an AI model through an API
* 📝 Displays AI-generated responses
* 🔐 Uses an environment variable for API key security
* 🧠 Supports conversational interaction
* ⚠️ Basic error handling
* 🚪 Allows the user to exit the chatbot
* 📚 Includes project documentation and setup instructions

---

## 🛠️ Technologies Used

* **Python**
* **AI API**
* **OpenAI Python SDK**
* **python-dotenv**
* **Git**
* **GitHub**
* **VS Code**

---

## 📂 Project Structure

```text
Python-Ai-Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env
└── screenshots/
    ├── 01_chatbot_working.png
    ├── 02_project_code.png
```

> **Important:** `.env` is used locally and must never be uploaded to GitHub.

---

## ⚙️ How It Works

The chatbot follows these steps:

### 1. User Input

The user enters a message in the chatbot.

### 2. API Request

The Python application sends the user's message to the AI API.

### 3. AI Processing

The AI model processes the request and generates a response.

### 4. Response

The chatbot receives the generated response from the API.

### 5. Display

The response is displayed to the user.

---

## 🔑 API Key Configuration

The API key is stored in a `.env` file instead of being directly written inside the Python source code.

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_api_key_here
```

The application loads the API key using `python-dotenv`.

### 🔒 Security

Never upload your actual API key to GitHub.

The `.env` file is included in `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Python-Ai-Chatbot.git
```

Move into the project directory:

```bash
cd Python-Ai-Chatbot
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure the API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key.

---

### 5. Run the Chatbot

```bash
python app.py
```

The chatbot will start and allow the user to enter messages and receive AI-generated responses.

---

## 📦 Dependencies

The main Python packages used in this project include:

```text
openai
python-dotenv
```

The complete dependency list is available in:

```text
requirements.txt
```

---

## 🔌 API Integration Approach

The project uses an AI API to communicate with an AI model.

The application:

1. Loads the API key securely from the `.env` file.
2. Initializes the AI API client.
3. Accepts the user's message.
4. Sends the message to the AI model.
5. Receives the model's response.
6. Displays the response to the user.

This demonstrates the basic concept of integrating an AI service into a Python application.

---

## 🧠 What I Learned

While developing this project, I learned about:

* Basic AI application development
* Working with AI APIs
* Sending requests to an AI model
* Handling API responses
* Using Python for AI integration
* Environment variables
* API key security
* Using `.gitignore`
* Managing Python dependencies
* Git and GitHub workflow
* Writing project documentation

---

## ⚠️ Challenges Faced

Some of the main challenges during development included:

* Understanding how AI API integration works
* Configuring the API key securely
* Managing Python dependencies
* Handling API-related errors
* Understanding the request and response flow between the application and AI model

These issues were resolved by referring to documentation, testing the application locally, and debugging the implementation.

---

## 🔮 Future Improvements

The chatbot can be improved further by adding:

* 🌐 Web-based user interface
* 💬 Better conversation history management
* 🎨 Improved chatbot UI
* ⏳ Loading indicators
* 📝 Markdown response support
* 🎤 Voice input
* 🔊 Voice output
* 💾 Chat history storage
* 🔐 Improved authentication and security
* ☁️ Cloud deployment

---

## 📸 Project Screenshots

### Chatbot Working

![Chatbot Working](screenshots/01_chatbot_working.png)

### Project Code

![Project Code](screenshots/02_project_code.png)

### GitHub Repository

![GitHub Repository](screenshots/03_github_repository.png)

---

## 🎯 Internship Task

**Internship:** AI Internship
**Task:** Day 1 Practical Assessment
**Task:** Build a Basic AI Chatbot

### Minimum Requirements Completed

* [x] Accept user message
* [x] Send message to AI model/API
* [x] Receive AI response
* [x] Display AI response
* [x] Working Python code
* [x] GitHub repository
* [x] README documentation
* [x] Secure API key using environment variables

---

## 👨‍💻 Author

**Purnoor Zafar**

B.E. Tech. Computer Engineering Technology

---

## 📄 License

This project is created for educational and internship purposes.
