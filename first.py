def display_question(question, choices):
    """Display the question and choices."""
    print(question)
    for idx, choice in enumerate(choices, start=1):
        print(f"{idx}. {choice}")

def get_answer(num_choices):
    """Get the user's answer and validate it."""
    while True:
        try:
            answer = int(input("Your choice (1/2/3/4): "))
            if 1 <= answer <= num_choices:
                return answer
            else:
                print(f"Please enter a number between 1 and {num_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    """Run the quiz and return the score."""
    score = 0
    for question, choices, correct_answer in questions:
        display_question(question, choices)
        user_answer = get_answer(len(choices))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
        print()  
    return score

def main():
    questions = [
        ("What is the tallest mountain in the world?", ["Denali", "Mount Everest", "Annapurna", "Aconcagua"], 2),
        ("Who was the first prime minister of India?", ["Indira Gandhi", "Morarji Desai", "Manmohan Singh", "Jawaharlal Nehru"], 4),
        ("Which is the oldest language of India?", ["Telugu", "Hindi", "Sanskrit", "Tamil"], 3),
        ("Who was the Author of Jana Gana Mana?", ["Rabindranath Tagore", "Anandmath", "Mohammad Iqbal", "Sri Aurobindo"], 1),
        ("Which is the national female animal of India?", ["Leopard", "Bengal Tiger", "Gharial", "Jacanas"], 2),
    ]

    print("Welcome to the Quiz Game!")
    print("========================\n")
    
    score = run_quiz(questions)
    
    print(f"Your final score is: {score}/{len(questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
