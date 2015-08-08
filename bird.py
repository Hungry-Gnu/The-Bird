import pygame
from constants import *
from colors import *
from bomb import Bomb
from sound import *



############################
###GET IMAGE FUNCTIONS######
def get_images_fly():

    image1 = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
    image2 = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
    images_list = [image1,image2]

    image1.fill(COLOR_WHITE)
    image1.set_colorkey(COLOR_WHITE)
    image2.fill(COLOR_WHITE)
    image2.set_colorkey(COLOR_WHITE)

    rect = pygame.Surface.get_rect(image1)
    x,y = rect.center
    y = y+8
    br = BODY_RADIUS

    pygame.draw.polygon(image1, COLOR_WING, ((x,y+br),(x+br, y-2*br), (x-br, y-2*br)))
    pygame.draw.circle(image1, COLOR_BODY, (x,y), br)
    pygame.draw.circle(image1, COLOR_EYE, (x-8,y-7), 4)
    pygame.draw.circle(image1, COLOR_EYE, (x+8,y-7), 4)
    pygame.draw.line(image1, COLOR_BEAK, (x+4,y-3), (x,y+12), 2)
    pygame.draw.line(image1, COLOR_BEAK, (x-4,y-3), (x,y+12), 2)
    pygame.draw.polygon(image1, COLOR_WING, ((x-20,y-7),(x-16, y+12),(x-40, y)))
    pygame.draw.polygon(image1, COLOR_WING, ((x+18,y-7),(x+16, y+12),(x+40, y)))

    pygame.draw.polygon(image2, COLOR_WING, ((x,y+br),(x+br, y-2*br), (x-br, y-2*br)))
    pygame.draw.circle(image2, COLOR_BODY, (x,y), br)
    pygame.draw.circle(image2, COLOR_EYE, (x-8,y-7), 4)
    pygame.draw.circle(image2, COLOR_EYE, (x+8,y-7), 4)
    pygame.draw.line(image2, COLOR_BEAK, (x+4,y-3), (x,y+12), 2)
    pygame.draw.line(image2, COLOR_BEAK, (x-4,y-3), (x,y+12), 2)
    pygame.draw.polygon(image2, COLOR_WING, ((x-20,y-7),(x-16, y+12),(x-30, y+20)))
    pygame.draw.polygon(image2, COLOR_WING, ((x+18,y-7),(x+16, y+12),(x+30, y+20)))

    return images_list

def get_image_sit():

    image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
    image.fill(COLOR_WHITE)
    image.set_colorkey(COLOR_WHITE)
    rect = pygame.Surface.get_rect(image)
    x,y = rect.center
    br = BODY_RADIUS
    pygame.draw.polygon(image, COLOR_WING, ((x,y+br),(x+br, y-2*br), (x-br, y-2*br)))
    pygame.draw.circle(image, COLOR_BODY, (x,y), br)
    pygame.draw.circle(image, COLOR_EYE, (x-8,y-7), 4)
    pygame.draw.circle(image, COLOR_EYE, (x+8,y-7), 4)
    pygame.draw.line(image, COLOR_BEAK, (x+4,y-3), (x,y+12), 2)
    pygame.draw.line(image, COLOR_BEAK, (x-4,y-3), (x,y+12), 2)
    pygame.draw.polygon(image, COLOR_WING, ((x-20,y-7),(x-16, y+12), (x-24, y+3)))
    pygame.draw.polygon(image, COLOR_WING, ((x+18,y-7),(x+16, y+12), (x+24, y+3)))

    return image

def get_image_dead():
    image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
    image.fill(COLOR_WHITE)
    image.set_colorkey(COLOR_WHITE)
    rect = pygame.Surface.get_rect(image)
    x,y = rect.center
    br = BODY_RADIUS
    #pygame.draw.polygon(image, COLOR_WING, ((x,y+br),(x+br, y-2*br), (x-br, y-2*br)))
    pygame.draw.circle(image, COLOR_BODY_DEAD, (x,y), br)
    pygame.draw.circle(image, COLOR_EYE, (x-8,y-7), 1)
    pygame.draw.circle(image, COLOR_EYE, (x+8,y-7), 1)
    pygame.draw.line(image, COLOR_BEAK, (x+4,y-3), (x,y+12), 2)
    pygame.draw.line(image, COLOR_BEAK, (x-4,y-3), (x,y+12), 2)
    pygame.draw.polygon(image, COLOR_WING, ((x-20,y-7),(x-16, y+12), (x-24, y+3)))
    pygame.draw.polygon(image, COLOR_WING, ((x+18,y-7),(x+16, y+12), (x+24, y+3)))

    return image

def get_image_placeholder(color):
    image_placeholder = pygame.Surface((BIRD_WIDTH//5, BIRD_HEIGHT//5))
    image_placeholder.fill(color)
    return image_placeholder

def get_image_shadow():

    image = pygame.Surface((2*BODY_RADIUS, int(BODY_RADIUS)))

    image.fill(COLOR_WHITE)
    image.set_colorkey(COLOR_WHITE)

    rect = pygame.Surface.get_rect(image)
    pygame.draw.ellipse(image, COLOR_GRAY, rect)
    image.set_alpha(50)

    return image



############################
###CLASS Bird###############
class Bird(pygame.sprite.Sprite):

    ############################
    ###CLASS CONSTANTS##########

    ENERGY_MAX = 1000
    CAPACITY_MAX = 1000
    SHIT_MAX = 1000

    TIME_FLY_MAX = 100
    TIME_CLICKS_MAX = 15

    #CALL GET IMAGE FUNCTIONS
    images_fly = get_images_fly()
    images_fly_number = len(images_fly)
    image_sit = get_image_sit()
    image_dead = get_image_dead()
   


    ############################
    ###INITIALISATION###########
    def __init__(self, game, screen, nest):
        super().__init__()
        self.game = game
        #SURFACE WHERE DRAW BIRD
        self.screen = screen
        #BIRD STATUS
        self.live = True
        #BIRD PERMISSIONS
        self.permission_to_fly = False
        self.permission_to_land_on_nest = False
        #BIRD LOCATION
        self.in_nest = True
        self.in_air = False
        self.in_fall = False
        self.on_land = False
        #BIRD ORDERS
        self.order_fly_up = False
        self.order_fly_to = None #Here x coordinate where bird is going to
        #BIRD PARAMETERS
        self.energy = ENERGY_MAXIMUM
        self.food = FOOD_MAXIMUM
        self.shit = 0
        #BIRD NEST COORDINATES
        self.nest = nest
        self.nest_xy_coordinates = nest.rect.midbottom
        #BIRD LEVELS OF FLYING, 0 IS GROUND
        self.y_levels = TUPLE_Y_LEVELS #constants.py
        self.index_level = 1 #0 is ground, 1 is nest, 3 is maximum
        #BIRD INITIAL COORDINATES
        self.x = self.nest_xy_coordinates[0]
        self.y = self.nest_xy_coordinates[1]
        #BIRD INITIAL RECTANGLE
        self.rect = pygame.Rect(0, 0, BIRD_WIDTH, BIRD_HEIGHT)
        self.rect.midbottom = self.x, self.y
        #BIRD INITIAL SPEED
        self.speed_x = 0
        self.speed_y = 0
        #ANIMATION COUNTER
        self.images_fly_counter = 0
        self.animation_rate = 1
        #TIME OF FLY
        self.time_fly = 0
        self.time_click = 0
        #SHADOW
        self.image_shadow = get_image_shadow()
        self.rect_shadow = pygame.Surface.get_rect(self.image_shadow)
        self.rect_shadow.bottom = self.y_levels[0]
        self.karr = pygame.mixer.Sound(file_karr)
        self.death_sound = pygame.mixer.Sound(file_death)
        self.death_sound.set_volume(0.2)


    ############################
    ###SPRITE UPDATE FUNCTION###
    def update(self):
        #USING FLY FUNCTIONS
        #Y MOVING
        #print(self.index_level, self.order_fly_up, self.in_air, self.in_fall)
        self.time_click += 1
        self.digest_food()
        self.get_permissions()
        #print('index_level', self.index_level, self.order_fly_up, self.in_air, self.in_fall, self.on_land)
        #print('permissions', self.permission_fly_up, self.permission_fly_ip, self.permission_run, self.permission_live)
        #print('time', self.time_fly)
        self.check_nest_landing()
        if self.order_fly_up:
            if self.permission_fly_up:
                if self.y > self.y_levels[self.index_level]:
                    self.fly_up()
                else:
                    self.order_fly_up = False
                    self.in_air = True
            else:
                self.index_level -=1
                self.order_fly_up = False
                self.in_fall = True

        elif self.in_air:
            if self.permission_fly_ip:
                if self.time_fly < self.TIME_FLY_MAX:
                    self.fly_in_place_y()
                    self.time_fly += 1
                else:
                    self.index_level -=1
                    self.in_air = False
                    self.in_fall = True
                    self.time_fly = 0   
            else:
                self.index_level -=1
                self.in_air = False
                self.in_fall = True
                self.time_fly = 0 

        elif self.in_fall:
            if self.y < self.y_levels[self.index_level]:
                self.fly_down()
            else:
                if self.index_level:
                    if self.permission_fly_ip:
                        self.in_fall = False
                        self.in_air = True
                    else:
                        self.index_level -= 1
                else:
                    self.in_fall = False
                    self.on_land = True
        elif self.on_land:
            self.sit()
            #print('nest')
        if self.live:
            if not self.permission_live:
                self.death()


        #X MOVING
        if self.order_fly_to:
            if self.in_nest:
                pass
            elif not self.on_land and self.permission_fly:
                if self.x < self.order_fly_to - 10:
                    self.fly_right()
                elif self.x > self.order_fly_to + 10:
                    self.fly_left()
                else:
                    self.order_fly_to = None
                    self.fly_in_place_x()
            elif self.on_land and self.permission_run:
                if self.x < self.order_fly_to - 10:
                    self.run_right()
                elif self.x > self.order_fly_to + 10:
                    self.run_left()
            else:
                    self.order_fly_to = None
 
        #MOVE BIRD RECTANGLE ACCORDING SPEED X AND Y
        self.rect.move_ip(self.speed_x, self.speed_y)
        self.x, self.y = self.rect.midbottom
        
        #MOVE SHADOW RECTANGLE
        self.rect_shadow.centerx = self.x
 
        #PREPARE IMAGE FOR DRAWING
        self.update_bird_image()
 
    def blit(self):
        if not self.in_nest:
            self.screen.blit(self.image_shadow, self.rect_shadow)
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, COLOR_WHITE, self.rect, 2)

    ################################
    ###UPDATE BIRD IMAGE FUNCTION###
    def update_bird_image(self):
        if self.live:
            if self.in_air or self.in_fall or self.order_fly_up:
                self.image = self.images_fly[self.images_fly_counter]
                self.animation_rate += 1
                if not self.animation_rate % ANIMATION_DIVIDER:
                    self.animation_rate = 1
                    self.images_fly_counter += 1
                    if not (self.images_fly_counter < self.images_fly_number):
                        self.images_fly_counter = 0
            else:
                self.image = self.image_sit
        else:
            self.image = self.image_dead




    ############################
    ###FLY FUNCTIONS############
    #Y-AXIS
    def fly_up(self):
        self.speed_y = -4 #pay atention constant
        self.energy -= ENERGY_FLY_UP + ENERGY_LIVE
    def fly_down(self):
        self.speed_y = 3
        self.energy -= ENERGY_LIVE
    def fly_in_place_y(self):
        self.speed_y = 0
        self.energy -= ENERGY_FLY_IN_PLACE + ENERGY_LIVE
    #X-AXIS
    def fly_right(self):
        self.speed_x = 4
        self.energy -= ENERGY_FLY + ENERGY_LIVE 
    def fly_left(self):
        self.speed_x = -4
        self.energy -= ENERGY_FLY + ENERGY_LIVE 
    def fly_in_place_x(self):
        self.speed_x = 0
    #SIT
    def run_right(self):
        self.speed_x = 2
        self.energy -= ENERGY_RUN + ENERGY_LIVE
    def run_left(self):
        self.speed_x = -2
        self.energy -= ENERGY_RUN + ENERGY_LIVE
    def sit(self):
        self.speed_y = 0
        self.speed_x = 0
        if self.live:
            self.energy -= ENERGY_LIVE
    ############################
    ###MOUSE CLICK ON BIRD######
    def mouse_click(self):

        if not self.order_fly_up and self.live:
            if self.index_level < len(self.y_levels)-1:
                if self.time_click < self.TIME_CLICKS_MAX:
                    self.order_fly_up = True
                    self.index_level += 1
                    self.on_land = False
                    self.in_air = False
                    self.in_fall = False
                    self.time_fly = 0
                elif not self.on_land and not self.in_fall:
                    self.in_air = True
                    self.time_fly = 0
                if self.in_nest:
                    self.in_nest = False
                self.time_click = 0
                    
    ############################
    ######TRANSFERS FUNCTION####
    def digest_food(self):
        if (self.food >= 0) and self.live:
            self.food -= 1
            if self.shit < SHIT_MAXIMUM:
                self.shit += 1
            else:
                self.drop_bomb()
            if self.energy < ENERGY_MAXIMUM:
                if self.energy < ENERGY_MAXIMUM - FOOD_TO_ENERGY:
                    self.energy += FOOD_TO_ENERGY
                else:
                    self.energy = ENERGY_MAXIMUM
            
    def drop_bomb(self):
        if (self.shit >= SHIT_IN_BOMB) and self.live:
            bomb = Bomb(self)
            self.game.bombs_sprite_group.add(bomb)
            self.shit -= SHIT_IN_BOMB
    ############################
    #####PERMISSIONS FUNCTION###
    def get_permissions(self):
        self.permission_live = self.live and (self.energy >= ENERGY_LIVE)
        self.permission_run =  self.live and (self.energy >= ENERGY_RUN + ENERGY_LIVE)
        self.permission_fly_ip = self.live and (self.energy >= ENERGY_FLY_IN_PLACE + ENERGY_LIVE)
        self.permission_fly = self.live and (self.energy >= ENERGY_FLY + ENERGY_LIVE)
        self.permission_fly_up =  self.live and (self.energy >= ENERGY_FLY_UP + ENERGY_LIVE)
    def death(self):
        if self.live:
            pygame.mixer.Sound.play(self.death_sound)
            self.live = False


    def check_nest_landing(self):
        if not self.in_nest:
            if self.permission_to_land_on_nest:
                if abs(self.rect.centerx - self.nest.rect.centerx) < 30:
                    if abs(self.rect.centery - self.nest.rect.centery) < 20:
                        self.reset()

    def reset(self):
        #BIRD PERMISSIONS
        self.permission_to_fly = False
        self.permission_to_land_on_nest = False
        #BIRD LOCATION
        self.in_nest = True
        self.in_air = False
        self.in_fall = False
        self.on_land = False
        #BIRD ORDERS
        self.order_fly_up = False
        self.order_fly_to = None #Here x coordinate where bird is going to
        self.index_level = 1 #0 is ground, 1 is nest, 3 is maximum
        #BIRD INITIAL COORDINATES
        self.x = self.nest_xy_coordinates[0]
        self.y = self.nest_xy_coordinates[1]
        #BIRD INITIAL RECTANGLE
        self.rect.midbottom = self.x, self.y
        #BIRD INITIAL SPEED
        self.speed_x = 0
        self.speed_y = 0
        #ANIMATION COUNTER
        self.images_fly_counter = 0
        #TIME OF FLY
        self.time_fly = 0
        self.time_click = 0 
        pygame.mixer.Sound.play(self.karr)               

        
        

