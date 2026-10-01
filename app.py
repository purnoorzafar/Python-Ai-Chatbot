import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer clearly and politely."
    }
]


def demo_response(user_input):
    text = user_input.lower().strip()

    if "hello" in text or text == "hi":
        return "Hello! I'm your AI Assistant. How can I help you today?"

    if "what is python" in text:
        return (
            "Python is a high-level programming language widely used "
            "for software development, automation, data analysis, and AI."
        )

    if "what is my name" in text or "do you know my name" in text:
        for message in messages:
            if message["role"] == "user":
                previous = message["content"].lower()

                if "my name is" in previous:
                    name = previous.split("my name is", 1)[1].strip()

                    if name:
                        return f"Your name is {name.title()}."

        return "You haven't told me your name yet."

    if "who are you" in text:
        return (
            "I'm a Python AI chatbot created as an internship "
            "practical project."
        )

    if "how are you" in text:
        return "I'm doing great! Thanks for asking."

    if "bye" in text:
        return "Goodbye! Have a great day."

    return (
        "I'm currently running in demo mode because the AI API "
        "is unavailable. Your message was received successfully."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({
            "response": "Please enter a message."
        })

    messages.append({
        "role": "user",
        "content": user_input
    })

    if client:

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            answer = response.choices[0].message.content

        except Exception:
            answer = demo_response(user_input)

    else:
        answer = demo_response(user_input)

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return jsonify({
        "response": answer
    })


@app.route("/clear", methods=["POST"])
def clear_chat():

    global messages

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Answer clearly and politely."
        }
    ]

    return jsonify({
        "status": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)