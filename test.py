import requests

BASE_URL = "http://127.0.0.1:5000"

# --- Helper function to display the quiz ---
def display_quiz(quiz_data):
    print("\nQuiz with Options:")
    for idx, q in enumerate(quiz_data, start=1):
        print(f"\n{q['number']}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")

# --- Get topic and difficulty input from user ---
topic = input("Enter a topic for the quiz: ")
difficulty = input("Enter the difficulty level for the quiz (e.g., Elementary School, Middle School, High School, College, PhD): ")

# --- Send request to generate quiz ---
quiz_response = requests.post(f"{BASE_URL}/quiz", json={"topic": topic, "difficulty": difficulty})

# --- Parse and display the quiz ---
if quiz_response.status_code == 200:
    quiz_data = quiz_response.json().get("quiz")
    
    if quiz_data:
        # Manually add the 'number' field for each question
        for idx, question in enumerate(quiz_data, start=1):
            question['number'] = f"Question {idx}"

        # Now display the quiz with the 'number' field added
        display_quiz(quiz_data)

        # --- Get student answers ---
        student_answers = []
        for q in quiz_data:
            while True:
                answer = input(f"Your answer for {q['number']} (A/B/C/D): ").upper()
                if answer in ['A', 'B', 'C', 'D']:
                    student_answers.append(answer)
                    break
                else:
                    print("Invalid input. Please enter one of the following: A, B, C, D")

        # --- Send student answers for grading ---
        grade_response = requests.post(f"{BASE_URL}/grade", json={"quiz": quiz_data, "student_answers": student_answers})

        if grade_response.status_code == 200:
            grade_data = grade_response.json()
            print("\nGrading Results:")
            for graded_answer in grade_data["graded_answers"]:
                print(f"Question: {graded_answer['question']}")
                print(f"Student's Answer: {graded_answer['student_answer']}")
                print(f"Correct Answer: {graded_answer['correct_answer']}")
                print(f"Score: {graded_answer['grade']}")
                
            print(f"\nOverall Score: {grade_data['overall_score']}%")
        else:
            print("Grading failed.")
    else:
        print("Quiz data was null.")
else:
    print("Request failed.")
