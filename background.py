import pygame
from constants import *
from colors import *
from tree import Tree

class Background:
    def __init__(self, screen):
        self.screen = screen
        #BLIT ALL BACKGROUND ELEMENTS ON BACKGROUND SURFACE
        self.surface = pygame.Surface(RESOLUTION)
        #FILL THE SURFACE WITH BLUE AS SKY
        self.surface.fill(COLOR_SKY)
        #DRAW GROUND 1/3 OF SKY AT BOTTOM ON THE SURFACE.
        pygame.draw.rect(self.surface, COLOR_GROUND, RECTANGLE_GROUND)
        #BLIT GRASS BEHIND TREES ON THE SURFACE
        #RECTANGLE_GRASS_BEHIND = None
        #grass_behind.blit(self.surface, RECTANGLE_GRASS_BEHIND, density, size)
        #BLIT TREE
        tree = Tree(self.surface, (TREE_X, TREE_Y))
        tree.blit()
        #DRAW NEST
        #nest.blit()
        #NOW WE GET THE SURFACE READY FOR THE GAME
    def blit(self):
        self.screen.blit(self.surface, (0,0))


