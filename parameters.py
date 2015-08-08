import pygame
from label import *
from bar import *

class Parameters():
    def __init__(self, screen, bird, FONT, FONT_SIZE, XY_TOPRIGHT):
        super().__init__()
        self.screen = screen
        self.bird = bird
        self.FONT = FONT
        self.FONT_SIZE = FONT_SIZE
        self.ALPHA = (70,70,70) #ANY NOT USED COLOR

        self.get_labels()
        self.get_bar_rect()
        self.get_offset()
        self.create_image_and_rect()
        self.get_bars()
        self.blit_labels()
        
        self.rect.topright = XY_TOPRIGHT
        
    def update(self):

        parameter = self.bird.energy//100
        self.bar_energy.update(parameter)
        self.bar_energy.blit()

        parameter = self.bird.food//10
        self.bar_food.update(parameter)
        self.bar_food.blit()

        parameter = self.bird.shit//10
        self.bar_shit.update(parameter)
        self.bar_shit.blit()

    def blit(self):
        self.screen.blit(self.image, self.rect)



    #INIT FUNCTIONS
    def get_labels(self):

        self.label_energy = Label(' E N E R G Y ', self.FONT, self.FONT_SIZE, COLOR_PARAMETERS)
        self.label_food = Label(' F O O D ', self.FONT, self.FONT_SIZE, COLOR_PARAMETERS)
        self.label_shit = Label(' P O O P ', self.FONT, self.FONT_SIZE, COLOR_PARAMETERS)

    def get_bar_rect(self):

        labels_h = self.label_energy.rect.h, self.label_food.rect.h, self.label_shit.rect.h
        label_h_max = max(labels_h)

        labels_w = self.label_energy.rect.w, self.label_food.rect.w, self.label_shit.rect.w
        label_w_max = max(labels_w)

        self.bar_rect = pygame.Rect(0, 0, label_w_max, label_h_max//2)

    def get_offset(self):
        self.offset = self.bar_rect.height // 3

    def get_bars(self):

        bar_rect = self.bar_rect
        offset = self.offset
        size = bar_rect.size
        x = offset

        y = offset + self.label_energy.rect.height + offset
        self.bar_energy = Bar(self.image, (x, y), size)

        y += bar_rect.height + offset + self.label_food.rect.height + offset
        self.bar_food = Bar(self.image, (x, y), size)

        y += bar_rect.height + offset + self.label_shit.rect.height + offset
        self.bar_shit = Bar(self.image, (x, y), size)

    def create_image_and_rect(self):

        bar_rect = self.bar_rect
        offset = self.offset

        leh = self.label_energy.rect.height
        lfh = self.label_food.rect.height
        lsh = self.label_shit.rect.height
        image_w = offset + bar_rect.w + offset
        image_h = offset + leh + offset + bar_rect.h + offset + lfh + offset + bar_rect.h + offset + lsh + offset + bar_rect.h + offset
        self.size = image_w, image_h
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect((0,0), self.size)
        self.image.fill(self.ALPHA)
        self.image.set_colorkey(self.ALPHA)

    def blit_labels(self):
        rect = self.label_energy.rect.copy()
        rect.centerx = self.rect.centerx
        x = rect.x
        y = self.offset
        self.image.blit(self.label_energy.image, (x, y))

        rect = self.label_food.rect.copy()
        rect.centerx = self.rect.centerx
        x = rect.x
        y += self.label_energy.rect.height + self.offset + self.bar_rect.height + self.offset
        self.image.blit(self.label_food.image, (x, y))

        rect = self.label_shit.rect.copy()
        rect.centerx = self.rect.centerx
        x = rect.x
        y += self.label_food.rect.height + self.offset + self.bar_rect.height + self.offset
        self.image.blit(self.label_shit.image, (x, y))
        
    




