class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_choice):
        return user_choice == self.correct_choice


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.question)
        for i, choice in enumerate(question.choices, start=1):
            print(f"{i}. {choice}")
        
        user_choice = int(input("Enter your choice (1/2/3): "))
        if user_choice > 0 and user_choice <= len(question.choices):
            if question.check_answer(user_choice):
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect.\n")
        else:
            print("Invalid choice. Moving to the next question.\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London"], 1)
    question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter"], 2)
    question3 = Question("Which famous scientist developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei"], 2)
    
    quiz_questions = [question1, question2, question3]
    
    print("Welcome to the Quiz Game!")
    run_quiz(quiz_questions)
