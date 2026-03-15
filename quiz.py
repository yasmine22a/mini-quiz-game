# quiz.py

# Liste de questions
questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["a) Seoul", "b) Tokyo", "c) Beijing"],
        "answer": "b"
    },
    {
        "question": "Which language is this quiz written in?",
        "options": ["a) Python", "b) C", "c) Java"],
        "answer": "a"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["a) 3", "b) 4", "c) 5"],
        "answer": "b"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (a/b/c): ").lower()
    if user_answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong ❌")
        
print(f"\nYour final score is: {score}/{len(questions)}")