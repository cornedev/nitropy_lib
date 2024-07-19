import pygame

def setWindowSize(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('nitropy game window')
    return screen

def setWindowTitle(title):
    pygame.display.set_caption(title)

def setWindowColor(screen, r, g, b):
    screen.fill((r, g, b))
    pygame.display.flip()
