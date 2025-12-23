import pygame
from time import sleep

def play_sound(location):
    pygame.mixer.init()
    pygame.mixer.music.load(location)
    pygame.mixer.music.play()
    sleep(3)


# Load and play the sound


# Keep the program running while the sound plays
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
