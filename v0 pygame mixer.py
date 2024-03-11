import pygame

pygame.init()
pygame.mixer.music.load("/Users/jonas/JONAS VETSCH/2_PRIVAT/5_Projekte/Coding Projects 2024/GPT Coding Interface/speech_output.mp3")


pygame.mixer.music.play()


while True:
    n = input("Type Play or Stop to start or stop the song. \nType Exit to stop the program:")
    if n == "play":
        pygame.mixer.music.play()
    elif n == "stop":
        pygame.mixer.music.pause()
    elif n == "exit":
        exit()