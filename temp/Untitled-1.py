

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        print(self.question)
        for option in self.options:
            print(f"{option}: {self.options[option]}")

        user_answer = input("Enter your answer: ")
        if user_answer == self.answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", self.answer)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def start(self):
        while self.current_question < len(self.questions):
            self.questions[self.current_question].ask()
            self.current_question += 1

        print("You have finished the quiz!")

def create_quiz():
    # Create a list of questions
    questions = []
    questions.append(Question("What is the capital of France?", {"A": "Paris", "B": "London", "C": "Berlin", "D": "Rome"}, "A"))
    questions.append(Question("What is the largest ocean in the world?", {"A": "Atlantic Ocean", "B": "Pacific Ocean", "C": "Indian Ocean", "D": "Arctic Ocean"}, "B"))
    questions.append(Question("What is the square root of 16?", {"A": "2", "B": "4", "C": "8", "D": "16"}, "A"))

    # Create a quiz object
    quiz = Quiz(questions)

    return quiz

if __name__ == "__main__":
    quiz = create_quiz()
    quiz.start()