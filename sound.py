import pygame
from time import sleep

def play_sound(location):
    pygame.mixer.init()
    pygame.mixer.music.load(location)
    pygame.mixer.music.play()
    sleep(3)
