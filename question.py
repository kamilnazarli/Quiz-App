from sound import play_sound
from time import sleep
class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options #["...", "...", "..."]
        self.correct_option = correct_option #[3]
        self.variants = ['A', 'B', 'C']
    def is_correct(self, answer):
        if self.variants.index(answer) == self.correct_option:
            play_sound("correctt.mp3")
            return True
        else:
            play_sound("wrong.mp3")
            return False
    def __str__(self):
        options = [f"{self.variants[i]}) {option}" for i, option in enumerate(self.options)]
        
        option_display = "\n".join(options)
        return f"{self.question}\n{option_display}"
