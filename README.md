# EC530_Final Project: AI-Powered Material Generator & Document Analyzer

This project is an tool that uses OpenAI’s GPT API to allows users to generate customized material and automatically grade, and analyze written documents for feedback. It is built using Python and Flask, making it easy to run locally and extend further for web or classroom use.

The motivation behind doing this project was to make it easier for educators to create material and grade students work. This AI tool can generate multiple choice questinos for any topic and difficulty level, provide solutions, and score each question. Please see below to understand how this AI system works, as well as the attached powerpoint  to see working examples. Furthermore, please see the Improvents section below for ideas on how to take this AI system to the next level. 
Please try out several different topics and difficulty levels to explore the functionality of this AI system. Hopefully, you find this to be as beneficial as I have. 

Thank You and Enjoy!

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

## File Descriptions

| File               | Purpose |
|--------------------|---------|
| `app.py`           | Main Flask server. Handles endpoints for quiz generation, grading, and essay feedback. |
| `test.py`          | Command-line interface for generating quizzes and submitting answers. |
| `llm_utils.py`     | Logic for calling the OpenAI API and generating quiz content using prompts. |
| `grading_utils.py` | Grades student quiz responses based on answer keys. Returns scores and correct answers. |
| `requirements.txt` | Contains all the systems neccessary to run this project. |

---

## Improvement Ideas 
- Generate more than 5 questions.
- Modify the material from multiple choice to short answer responses.
- Output the exam/quiz as a word file so the instructor can physically print out the exam/quiz and use it in class.
- Create an upload feature where the AI takes a word, excel, text, etc file and then grades the students answers.
- If a student gets an incorrect answer, the AI provides an explanation on why that is wrong and what the correct answer should be. 
