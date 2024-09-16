from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    text = data["question"]
    answer = data["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

Keep_ask = True
quiz = QuizBrain(question_bank)
while Keep_ask:
    quiz.next_question()
    Keep_ask = quiz.still_has_questions()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
