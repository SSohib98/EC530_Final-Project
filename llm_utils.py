import os
from openai import OpenAI, OpenAIError
import json

# Create the OpenAI client using your API key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt, temperature=0.7):
    try:
        # Debug: print the prompt being sent to the API
        print("Sending prompt to OpenAI:\n", prompt)

        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )

        # Print the raw response object for debugging
        print("Raw Response:", response)

        # ✅ Correct usage with new SDK object response
        return response.choices[0].message.content.strip()

    except OpenAIError as e:
        print("Error:", e)
        return None

def generate_quiz(topic, difficulty='High School'):
    # Modify the prompt to include difficulty level and request structured JSON output
    prompt = f"""Create a 5-question multiple-choice quiz about {topic} suitable for {difficulty} students.
Each question should have four options labeled A–D. Include the correct answer in the format: "A", "B", "C", or "D".
Return the quiz as a JSON object with the following structure:
[
    {{
        "question": "The question text",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "A"  # The correct answer, e.g. "A"
    }},
    ...
]
"""

    print(f"Generating quiz with the following prompt:\n{prompt}")

    quiz = call_llm(prompt)

    if not quiz:
        print("Quiz generation failed or returned empty result.")
        return {"quiz": None}

    # Parse the LLM response as JSON and return it as a structured object
    try:
        quiz_data = json.loads(quiz)
        return {"quiz": quiz_data}
    except Exception as e:
        print(f"Error parsing the quiz JSON: {e}")
        return {"quiz": None}

# Optional: Run standalone to test quiz generation
if __name__ == "__main__":
    quiz = generate_quiz("machine learning", "High School")
    print("Generated Quiz:", quiz)
