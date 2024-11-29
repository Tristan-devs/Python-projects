def welcome_message():
    print("Welcome to the Simple Quiz Application!")

def display_question(question, options):
    print(f"\n{question}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

def get_user_input(num_options):
    while True:
        try:
            choice = int(input("Your answer (1-4): "))
            if 1 <= choice <= num_options:
                return choice
            else:
                print("Invalid input. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_score(questions):
    score = 0
    for question, data in questions.items():
        display_question(question, data['options'])
        user_choice = get_user_input(len(data['options']))
        if data['options'][user_choice - 1] == data['answer']:
            score += 1
    return score

def display_results(score, total_questions):
    print("\nQuiz completed!")
    print(f"Your total score is: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You got all the answers correct!")
    elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

def thank_you_message():
    print("Thank you for taking the quiz!")

def main():
    questions = {
        "What is the capital of France?": {
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        "What is the largest ocean on Earth?": {
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        "What is the chemical symbol for gold?": {
            "options": ["Au", "Ag", "Pb", "Fe"],
            "answer": "Au"
        },
        "Who wrote 'Romeo and Juliet'?": {
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "answer": "William Shakespeare"
        }
    }

    welcome_message()
    score = calculate_score(questions)
    display_results(score, len(questions))
    thank_you_message()

if __name__ == "__main__":
    main()


