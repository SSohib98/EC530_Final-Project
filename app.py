from flask import Flask, request, jsonify
from llm_utils import generate_quiz
from grading_utils import grade_quiz  # Import the grade_quiz function
from feedback_utils import give_feedback

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    content = request.json.get("text")
    return jsonify(analyze_text(content))

@app.route("/quiz", methods=["POST"])
def quiz():
    topic = request.json.get("topic")
    difficulty = request.json.get("difficulty")  # Get difficulty level from user input
    return jsonify(generate_quiz(topic, difficulty))  # Pass difficulty to generate_quiz function


@app.route("/summary", methods=["POST"])
def summary():
    content = request.json.get("text")
    return jsonify({"summary": summarize_text(content)})

@app.route("/grade", methods=["POST"])
def grade():
    data = request.json
    quiz = data["quiz"]  # The full quiz
    student_answers = data["student_answers"]  # The student's answers to the questions
    return jsonify(grade_quiz(quiz, student_answers))  # Pass both quiz and answers to grading function

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    return jsonify(give_feedback(data["student_text"]))

if __name__ == "__main__":
    app.run(debug=True)
