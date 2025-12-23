from Quiz import Quiz
from leaderboard import LeaderBoard
from time import sleep
def main():
    print("Welcome to the quiz app.")
    while True:
        print("""\nOptions
1. Start the quiz
2. Check leaderboard
3. Exit\n
""")
        choice = input("Enter your choice: ")
        if (choice == '1'):
            quiz = Quiz("questions.txt")
            quiz.start()
        elif (choice == '2'):
            LeaderBoard.show()
        else:
            print("See you later")
            
            break
        
        sleep(2)


if (__name__ == "__main__"):
    main()