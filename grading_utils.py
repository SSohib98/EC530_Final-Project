from llm_utils import call_llm

def grade_answer(question, student_answer, answer_key):
    # Validate student_answer
    if student_answer not in ["A", "B", "C", "D"]:
        return "Invalid answer. Please answer with A, B, C, or D."
    
    # Check if the student's answer is correct or incorrect
    return student_answer == answer_key

def grade_quiz(quiz, student_answers):
    total_score = 0
    graded_answers = []

    # Loop through each question and grade it
    for idx, (question, student_answer) in enumerate(zip(quiz, student_answers)):
        correct_answer = question["answer"]

        # Skip invalid answers
        if student_answer not in ["A", "B", "C", "D"]:
            graded_answers.append({
                "question": question["question"],
                "student_answer": student_answer,
                "correct_answer": correct_answer,
                "is_correct": "Invalid",
                "grade": 0
            })
            continue

        # Check if the answer is correct or incorrect
        is_correct = grade_answer(question["question"], student_answer, correct_answer)
        
        # Update total score
        score = 1 if is_correct else 0
        total_score += score

        graded_answers.append({
            "question": question["question"],
            "student_answer": student_answer,
            "correct_answer": correct_answer,
            "is_correct": "Correct" if is_correct else "Incorrect",
            "grade": score
        })

    # Calculate the overall percentage score
    overall_score = (total_score / (len(quiz) * 1)) * 100

    return {"graded_answers": graded_answers, "overall_score": overall_score}
