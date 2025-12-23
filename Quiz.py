from question import Question
from leaderboard import LeaderBoard
import random
import time
from sound import play_sound
class Quiz:
    def __init__(self, question_file):
        self.question_file = question_file
        self.questions = []
        self.load_questions()
    def load_questions(self):
        try:
            with open(self.question_file) as file:
                for line in file:
                    parts = line.strip().split("|")
                    question_text = parts[0]
                    options = parts[1 : 4]
                    correct_option = options.index(parts[4])

                    question = Question(question_text, options, correct_option)
                    self.questions.append(question)
        except Exception as e:
            print(e)
            print("Error in loading questions...")
    def start(self):
        self.nickname = input("Enter your nickname: ")

        random.shuffle(self.questions)
        score = 0
        start_time = time.time()

        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question}")

            try:
                answer = input("Your answer: ")
                if answer not in question.variants:
                    raise ValueError("The input is not correct...")
                if question.is_correct(answer):
                    score += 1                
            except Exception as e:
                print(e)
                print("The input is not correct, please enter correct input.")
        end_time = time.time()
        duration = round(end_time - start_time)
        print(f"Quiz is finished.Your result {score}/5.({LeaderBoard.change_format(duration)} - the time that you used)")
        if score == 5:
            play_sound("correct.wav")
        self.save_score(self.nickname, score, duration)###########
    
    def save_score(self, nickname, score, duration):
        with open("leaderboard.txt", "a") as file:
            file.write(f"{nickname}|{score}|{duration}\n")
        print("Your score has been saved.")




                     

        

