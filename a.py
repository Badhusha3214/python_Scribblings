def run_simple_quiz(questions):
    score = 0
    atm = 0


    for question, correct_answer in questions.items():
        while True:
            atm += 1
            if atm > 3:
                    break
            print(question)
            user_answer = input("Your answer: ")

            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
                break
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")

    print(f"Quiz completed! Your score is: {score}")

simple_quiz_questions = {
        "What is the capital of France?": "a",
        "Which planet is known as the Red Planet?": "a",
        "What is the largest mammal in the world?": "b",
    }

run_simple_quiz(simple_quiz_questions)
