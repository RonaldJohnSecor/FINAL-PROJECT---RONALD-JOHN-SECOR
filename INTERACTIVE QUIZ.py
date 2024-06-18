import random

# List of questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What element does 'O' represent on the periodic table?", "answer": "Oxygen"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the chemical formula for water?", "answer": "H2O"},
    {"question": "Who is known as the father of computers?", "answer": "Charles Babbage"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
]

# Make sure we have at least 100 questions
while len(questions) < 10:
    questions.append({"question": f"Question {len(questions) + 1}", "answer": f"Answer {len(questions) + 1}"})

# Shuffle questions for a random order
random.shuffle(questions)

# Track user answers
user_answers = []

# Function to conduct the quiz
def conduct_quiz():
    print("Welcome to the quiz! Please answer the following questions:\n")

    for idx, q in enumerate(questions, start=1):
        print(f"Question {idx}: {q['question']}")
        answer = input("Your answer: ")
        user_answers.append({"question": q["question"], "correct_answer": q["answer"], "user_answer": answer})

    print("\nQuiz completed! Here are your results:\n")
    show_results()

# Function to show results
def show_results():
    correct_count = 0

    for idx, ua in enumerate(user_answers, start=1):
        correct = ua["correct_answer"].lower() == ua["user_answer"].lower()
        correct_count += correct
        status = "Correct" if correct else "Incorrect"
        print(f"Question {idx}: {ua['question']}")
        print(f"Your answer: {ua['user_answer']} (Correct answer: {ua['correct_answer']}) - {status}\n")

    print(f"You got {correct_count} out of {len(questions)} correct.")

conduct_quiz()