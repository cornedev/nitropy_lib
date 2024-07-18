import pygame

def setWindowSize(x, y):
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("nitropy game window")
    return screen
