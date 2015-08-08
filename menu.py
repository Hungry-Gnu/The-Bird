import pygame
import sys
from clock_and_screen import clock_and_screen
from colors import *
from bird import get_image_sit
from button import Button
from fonts import *
from game import *
from sound import *



class Menu:

    def __init__(self, clock_and_screen):
        self.screen = clock_and_screen[1]
        self.clock = clock_and_screen[0]
        self.init_labels()
        self.init_buttons()
        self.init_picture()
        self.init_score_label()
        self.pause = False
        self.game = None
        self.start_music()
    def start_music(self):
        #MUSIC
        pygame.mixer.music.load(file_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)



    #Initialisation functions
    def init_picture(self):
        bird_image = get_image_sit()
        size = list(bird_image.get_size())
        for i in range(0,len(size)):
            size[i] = 3 * size[i]
        self.bird_image = pygame.transform.scale(bird_image, size)
    def init_labels(self):
        pass
    def init_buttons(self):
        self.button_group = pygame.sprite.Group()
        rect = [40,300,300,100]
        play_button = Button(self.screen, rect, FONT_MAIN, 50, 'PLAY', COLOR_MENU_GREEN, COLOR_MENU_BLUE, COLOR_MENU_YELLOW, self.play)
        self.button_group.add(play_button)
        rect[0] = 4* rect[0] + rect[2]
        quit_button = Button(self.screen, rect, FONT_MAIN, 50, 'QUIT', COLOR_MENU_RED, COLOR_MENU_BLUE, COLOR_MENU_YELLOW, self.exit)
        self.button_group.add(quit_button)

    #Main loop
    def loop(self):
        while True:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(50)

    #Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
    #The exit function
    def exit(self):
        pygame.quit()
        sys.exit()

    #Play function
    def play(self):
        if self.pause:
            self.pause = self.game.loop()
            
        else:
            if self.game:
                del self.game
            self.game = Game(self.clock, self.screen)
            self.pause = self.game.loop()
        self.score_label.update(self.game.score)
        

        


    def update(self):
        self.button_group.update()
        
    def draw(self):
        self.screen.fill(COLOR_MENU)
        x, y = self.screen.get_size()
        w_bird = self.bird_image.get_width()
        
        position = x//2 - w_bird//2, y//10
        self.screen.blit(self.bird_image, position)

        self.button_group.draw(self.screen)

        if self.game:
            self.score_label.draw(self.screen)
        pygame.display.update()

    def init_score_label(self):
        #self.score_label_group = pygame.sprite.GroupSingle
        self.score_label = Score_label(250,250, 'YOU POOPED === ', ' === CATS!')
        #self.score_label_group.add(score_label)
        self.score = 0


menu = Menu(clock_and_screen())
menu.loop()
