class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer=input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, corrent_answer):
        answer = self.questions[self.question_number - 1].answer
        if user_answer.lower() ==corrent_answer.lower():
            self.score += 1
            print('Correct!')
        else:
            print(f'Incorrect, the correct answer was {corrent_answer}')