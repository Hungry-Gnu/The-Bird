import pygame
from constants import *
from colors import *

class Tree:
#This is a tree class
	def __init__(self, screen, xy_middlebotom):
		self.xy_middlebotom = xy_middlebotom
		self.screen = screen

	def blit(self):
		'''DRAWS A TREE (x,y,screen=screen)
		x and y the bottom middle'''
		screen = self.screen
		x = self.xy_middlebotom[0]
		y = self.xy_middlebotom[1]

		#SIZE OF THE TREE
		WIDTH = TREE_WIDTH
		HEIGHT = TREE_HEIGHT
		#COORDINATES OF THE TRUNK
		t_x1 = x + WIDTH//5
		t_y1 = y
		t_x2 = x + WIDTH//10
		t_y2 = y - HEIGHT
		t_x3 = x - WIDTH//10
		t_y3 = t_y2
		t_x4 = x - WIDTH//5
		t_y4 = y
		#COORDINATES OF BRANCHES
		br_x1 = x + WIDTH//8
		br_y1 = y - HEIGHT//2
		br_x2 = x + 3*WIDTH//7
		br_y2 = y - 5*HEIGHT//7
		bl_x1 = x
		bl_y1 = y - 2*HEIGHT//3
		bl_x2 = x - WIDTH//3
		bl_y2 = y - 8*HEIGHT//9
		#COORDINATES OF THE LEAVES
		lt_x = x + WIDTH//8
		lt_y = y - HEIGHT
		lr_x = x + 4*WIDTH//9
		lr_y = y - 9*HEIGHT//12
		ll_x = x - 5*WIDTH//12
		ll_y = y - 11*HEIGHT//12

		#DRAW THE BRANCHES
		pygame.draw.line(screen, COLOR_BRANCH, (br_x1, br_y1), (br_x2, br_y2), 22)
		pygame.draw.line(screen, COLOR_BRANCH, (bl_x1, bl_y1), (bl_x2, bl_y2), 18)    

		#DRAW THE TRUNK
		pygame.draw.polygon(screen, COLOR_TRUNK, ((t_x1, t_y1),(t_x2, t_y2),\
				(t_x3, t_y3),(t_x4, t_y4)))
		#DRAW THE LEAVES
		pygame.draw.circle(screen, COLOR_LEAVES1, (lt_x,lt_y),48)
		pygame.draw.circle(screen, COLOR_LEAVES2, (ll_x,ll_y),38)
		pygame.draw.circle(screen, COLOR_LEAVES3, (lr_x,lr_y),42)

