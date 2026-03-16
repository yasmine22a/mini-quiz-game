quiz_categories = {
    "Capitals": [
        {
            "question": "What is the capital of Japan?",
            "options": ["a) Seoul", "b) Tokyo", "c) Beijing"],
            "answer": "b"
        },
        {
            "question": "What is the capital of France?",
            "options": ["a) Paris", "b) Lyon", "c) Marseille"],
            "answer": "a"
        },
        {
            "question": "What is the capital of South Korea?",
            "options": ["a) Seoul", "b) Berlin", "c) Ottawa"],
            "answer": "a"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["a) Seoul", "b) Berlin", "c) Canberra"],
            "answer": "c"
        },
        {
            "question": "What is the capital of Vietnam?",
            "options": ["a) Lima", "b) Hanoi", "c) Ottawa"],
            "answer": "b"
        }
    ],
    "Math": [
        {
            "question": "2 + 2 = ?",
            "options": ["a) 3", "b) 4", "c) 5"],
            "answer": "b"
        },
        {
            "question": "5 * 3 = ?",
            "options": ["a) 15", "b) 10", "c) 8"],
            "answer": "a"
        },
        {
            "question": "50 + 250 = ?",
            "options": ["a) 311", "b) 300", "c) 299"],
            "answer": "b"
        }
    ],
    "Programming": [
        {
            "question": "Which language is this quiz written in?",
            "options": ["a) Python", "b) C", "c) Java"],
            "answer": "a"
        }
    ]
}

# Display categories
print("Choose a quiz category:")
for i, category in enumerate(quiz_categories.keys(), start=1):
    print(f"{i}) {category}")

# User selects category
choice = input("Enter the number of your category: ")

# Validate choice
try:
    choice_index = int(choice) - 1
    category_name = list(quiz_categories.keys())[choice_index]
except (ValueError, IndexError):
    print("Invalid choice. Exiting quiz.")
    exit()

# Run quiz
questions = quiz_categories[category_name]
score = 0

print(f"\nYou chose the category: {category_name}")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (a/b/c): ").lower()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong.")

print(f"\nYour final score is: {score}/{len(questions)}")