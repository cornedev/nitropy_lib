import pygame

def setWindowSize(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('nitropy game window')
    return screen
