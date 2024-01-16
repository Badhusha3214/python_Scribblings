class MCQQuiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.attempts = 3

    def run_quiz(self):
        for question, options in self.questions.items():
            print(question)
            self.attempts = 3
            while self.attempts > 0:
                self.display_options(options)
                user_answer = input("Your answer (A, B, C, or D): ").upper()
                correct_answer = self.questions[question]["correct"].upper()

                if user_answer == correct_answer:
                    print("Correct!\n")
                    self.score += 1
                    break
                else:
                    self.attempts -= 1
                    if self.attempts > 0:
                        print(f"Wrong! You have {self.attempts} attempts left. Try again.\n")
                    else:
                        print(f"Wrong! The correct answer is: {correct_answer}\n")

    def display_options(self, options):
        for option, value in options.items():
            print(f"{option}. {value}")
        print()

    def display_score(self):
        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Define your MCQ quiz questions and answers here
    mcq_quiz_questions = {
        "What is the capital of France?": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid", "correct": "C"},
        "Which planet is known as the Red Planet?": {"A": "Mars", "B": "Venus", "C": "Jupiter", "D": "Saturn", "correct": "A"},
        "What is the largest mammal in the world?": {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Panda", "correct": "B"},
    }

    # Create an MCQQuiz object and run the quiz
    mcq_quiz = MCQQuiz(mcq_quiz_questions)
    mcq_quiz.run_quiz()

    # Display the final score
    mcq_quiz.display_score()
