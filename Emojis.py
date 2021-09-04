import emoji
import pygame
print(emoji.emojize('Python is :grinning:', use_aliases=True)) #https://pypi.org/project/emoji/
print(emoji.emojize("Emoji não apareceu colorido :cry:", use_aliases=True))
print('\033[1;33;44mToca um som aeh Python')
pygame.mixer.init()
pygame.mixer.music.load('Trips.mp3')
pygame.mixer.music.play()
input()
#pygame.event.wait()
print('\033[1;33;44mValeu! Esse Python é foda!')