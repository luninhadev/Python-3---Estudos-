#  DESAFIO 021

# Faça um programa que abra e reproduza o áudio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021KDA-MORE.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.event.wait()


""" NÃO FUNCIONOU:
from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3('ex021KDA-MORE.mp3')
print('Musica usando pydub')
play(song)
"""
