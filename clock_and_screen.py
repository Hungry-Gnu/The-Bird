import pygame
from constants import *

def clock_and_screen():
    #PYGAME INITIALISATION
    pygame.init()
    #SCREEN SURFACE INITIALISATION
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("The Bird")
    #CLOCK INITIALISATION
    clock = pygame.time.Clock()
    return clock, screen
