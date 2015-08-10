import pygame
import sys
import random
from clock_and_screen import clock_and_screen
from background import Background
from nest import Nest
from bird import Bird
from constants import *
from worm import Worm
from fonts import *
from parameters import Parameters
from cat import Cat
from shadow import Shadow
from score_label import Score_label
from flag import Flag
from sound import *
#

class Game:
    #clock, screen = clock_and_screen()
    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        self.time_after_end = TIME_AFTER_END
        self.init_bg()
        self.init_nest()
        self.init_flag()
        self.init_bird()
        self.init_worms()
        self.init_cats()
        self.init_parameters()
        self.init_bombs()
        self.init_score_label()
        self.game_ended = False
        self.hit = pygame.mixer.Sound(file_hit)
    def loop(self):
        while not self.game_ended:
                self.end()
                self.events()
                self.update()
                self.draw()
                self.clock.tick(50)


    #The loop functions
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.mouseclick_on_bird():
                        self.bird.mouse_click()
                    else:
                        self.bird.order_fly_to = pygame.mouse.get_pos()[0]
                        if self.mouseclick_on_nest():
                            self.bird.permission_to_land_on_nest = not self.bird.permission_to_land_on_nest

                elif pygame.mouse.get_pressed()[2]:
                    self.bird.drop_bomb()


    def update(self):
        if self.bird.live:
            self.cats_vs_bird()
        self.bombs_vs_cats()
        self.bird.update()
        self.bombs_sprite_group.update()
        self.worms_update()
        self.cats_update()
        self.bird_eat_worm()
        self.parameters.update()
        self.score_label.update(self.score)
        self.clear_cats_if_more_than_30()
    def draw(self):
        self.bg.blit()
        self.nest.blit()
        if self.bird.permission_to_land_on_nest:
            self.flag.blit()
        self.worms_sprite_group.draw(self.screen)
        self.cats_shadows_sprite_group.draw(self.screen)
        self.bird.blit()
        self.cats_sprite_group.draw(self.screen)
        self.bombs_sprite_group.draw(self.screen)
        self.parameters.blit()
        self.score_label.draw(self.screen)
        pygame.display.update()
    #The exit function
    def exit(self):
        pygame.quit()
        sys.exit()
    #The init functions
    def init_bg(self):
        self.bg = Background(self.screen)
    def init_nest(self):
        self.nest = Nest(self.screen, NEST_XY)
    def init_flag(self):
        self.flag = Flag(self.nest)
    def init_bird(self):
        self.bird = Bird(self, self.screen, self.nest)
    def init_worms(self):
        self.worms_sprite_group = pygame.sprite.Group()
        worm = Worm()
        self.worms_sprite_group.add(worm)
        self.time_worm_creation = random.randint(WORM_CREATE_MIN, WORM_CREATE_MAX)

    def init_cats(self):

        #CAT INIT
        cat = Cat()
        self.cats_sprite_group = pygame.sprite.Group()
        self.cats_sprite_group.add(cat)
        self.time_cat_creation = random.randint(CAT_CREATE_MIN, CAT_CREATE_MAX)

        #CAT SHADOW INIT
        shadow = Shadow(cat)
        self.cats_shadows_sprite_group = pygame.sprite.Group()
        self.cats_shadows_sprite_group.add(shadow)

    def init_parameters(self):
        self.parameters = Parameters(self.screen, self.bird, FONT_MAIN, FONT_SIZE_COORD, (RESOLUTION[0], 0))
    def init_bombs(self):
        self.bombs_sprite_group = pygame.sprite.Group()
    def init_score_label(self):
        #self.score_label_group = pygame.sprite.GroupSingle
        self.score_label = Score_label(10,10, 'Scores:', '')
        #self.score_label_group.add(score_label)
        self.score = 0
    #Event functions
    def mouseclick_on_bird(self):
        mouse_xy = pygame.mouse.get_pos()
        click = self.bird.rect.collidepoint(mouse_xy)
        return click
    def mouseclick_on_nest(self):
        mouse_xy = pygame.mouse.get_pos()
        click = self.nest.rect.collidepoint(mouse_xy)
        return click
    #Worms creation function
    def worms_new(self):
        if self.time_worm_creation <= 0:
            worm = Worm()
            self.worms_sprite_group.add(worm)
            self.time_worm_creation = random.randint(WORM_CREATE_MIN, WORM_CREATE_MAX)
    #Worms update function
    def worms_update(self):
        self.worms_new()
        self.worms_sprite_group.update()
        self.time_worm_creation -= 1
    #Bird eat or not eat a worm
    def bird_eat_worm(self):
        worm_eaten = pygame.sprite.spritecollideany(self.bird, self.worms_sprite_group)
        if worm_eaten and self.bird.live:
            worm_eaten.kill()
            del worm_eaten
            self.bird.food += WORM_TO_FOOD
    #Cats creation function
    def cats_new(self):
        if self.time_cat_creation <= 0:
            #CAT CREATE
            cat = Cat()
            self.cats_sprite_group.add(cat)
            self.time_cat_creation = random.randint(CAT_CREATE_MIN, CAT_CREATE_MAX)
            #CAT SHADOW CREATE
            shadow = Shadow(cat)
            self.cats_shadows_sprite_group.add(shadow)
    #Cats update function
    def cats_update(self):
        #CATS UPDATE
        self.cats_new()
        self.cats_sprite_group.update()
        self.time_cat_creation -= 1
        #SHADOWS UPDATE
        self.cats_shadows_sprite_group.update()
    def cats_vs_bird(self):
        bird_eaten = pygame.sprite.spritecollideany(self.bird, self.cats_sprite_group)
        if bird_eaten:
            self.bird.death()
            bird_eaten.speed_x = 0
            bird_eaten.eat = True
    def bombs_vs_cats(self):
        shitted_cats =  pygame.sprite.groupcollide(self.bombs_sprite_group, self.cats_sprite_group, True, True)
        if shitted_cats:
            pygame.mixer.Sound.play(self.hit)
            for x in shitted_cats:
                self.score += len(shitted_cats[x])

    def clear_cats_if_more_than_30(self):
        if len(self.cats_sprite_group.sprites()) > 30:
            self.cats_sprite_group.clear()

    def end(self):
        if not self.bird.live:
            if self.time_after_end < 0:
                self.game_ended = True
            else:
                self.time_after_end -= 1
    




        


