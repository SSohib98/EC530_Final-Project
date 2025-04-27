# EC530_Final Project: AI-Powered Material Generator & Document Analyzer

This project is an tool that uses OpenAI’s GPT API to allows users to generate customized material and automatically grade, and analyze written documents for feedback. It is built using Python and Flask, making it easy to run locally and extend further for web or classroom use.

---

## Features

- Generate multiple-choice quizzes on any topic and difficulty level  
- Automatically grade student answers with accuracy  
- Simple command-line interface to interact with the system  
- RESTful API backend for easy integration with other applications  

---

## How to Set Up and Run

1. **Clone this repository:**

   `git clone https://github.com/your-username/final-project.git`  
   `cd final-project`

2. **Install the required libraries:**

   `pip install requirements.txt`

3. **Set your OpenAI API Key as an environment variable:**

   On Windows:  
   `set OPENAI_API_KEY=your_openai_key_here`

   On macOS/Linux:  
   `export OPENAI_API_KEY="your_openai_key_here"`

5. **Start the Flask server:**

   `python app.py`

6. **Run the quiz system from the command line:**

   `python test.py`

---

## How It Works

When you run the system:

- You’ll be prompted to enter a **topic** and **difficulty level**.  
- The app will use OpenAI to generate a 5-question multiple-choice quiz.  
- You’ll enter your answers (A/B/C/D).  
- The system grades your answers and returns your score.  

---

## 📂 File Descriptions

| File               | Purpose |
|--------------------|---------|
| `app.py`           | Main Flask server. Handles endpoints for quiz generation, grading, and essay feedback. |
| `test.py`          | Command-line interface for generating quizzes and submitting answers. |
| `llm_utils.py`     | Logic for calling the OpenAI API and generating quiz content using prompts. |
| `grading_utils.py` | Grades student quiz responses based on answer keys. Returns scores and correct answers. |
| `requirements.txt` | Contains all the systems neccessary to run this project. |

---
