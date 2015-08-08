import pygame
import random
from colors import *
from constants import *
from sound import *

def get_cat_images():

    image1 = pygame.Surface(CAT_SIZE)
    image1.fill(COLOR_WHITE)
    image1.set_colorkey(COLOR_WHITE)

    image2 = image1.copy()
    image3 = image1.copy()

    #IMAGE1 DRAWING##############################################
    #TAIL
    pygame.draw.line(image1, COLOR_CAT_HEAD, (102,30),(102,0),8)
    #FAR LEGS
    pygame.draw.line(image1, COLOR_CAT_HEAD, (34,50),(34,80),6)
    pygame.draw.line(image1, COLOR_CAT_HEAD, (92,50),(92,80),6)

    #BODY
    pygame.draw.rect(image1, COLOR_CAT_BODY, (30,30,80,22)) #CAT_BODY_RECT = (30,30,80,22)
    #NEAR LEGS
    pygame.draw.line(image1, COLOR_CAT_HEAD, (44,50),(44,80),6)
    pygame.draw.line(image1, COLOR_CAT_HEAD, (101,50),(101,80),6)
    #HEAD
    pygame.draw.circle(image1, COLOR_CAT_HEAD, (22,30), 22)
    #EARS
    pygame.draw.polygon(image1, COLOR_CAT_HEAD, ((2,20),(7,17),(3,5)))
    pygame.draw.polygon(image1, COLOR_CAT_BODY, ((12,10),(7,17),(3,5)))

    pygame.draw.polygon(image1, COLOR_CAT_HEAD, ((37,15),(43,6),(43,23)))
    pygame.draw.polygon(image1, COLOR_CAT_BODY, ((37,15),(43,6),(35,11)))
    #NOSE
    pygame.draw.circle(image1, COLOR_BLACK, (22,26), 4)
    pygame.draw.circle(image1, COLOR_BLACK, (17,30), 6, 2)
    pygame.draw.circle(image1, COLOR_BLACK, (27,30), 6, 2)
    #EYES
    pygame.draw.circle(image1, COLOR_BLACK, (14,20), 3)
    pygame.draw.circle(image1, COLOR_BLACK, (30,20), 3)    
    #MOUSTACHE
    pygame.draw.line(image1, COLOR_BLACK, (17,28),(4,25),2)
    pygame.draw.line(image1, COLOR_BLACK, (15,30),(2,30),2)
    pygame.draw.line(image1, COLOR_BLACK, (17,32),(4,35),2)


    pygame.draw.line(image1, COLOR_BLACK, (27,28),(40,25),2)
    pygame.draw.line(image1, COLOR_BLACK, (29,30),(42,30),2)
    pygame.draw.line(image1, COLOR_BLACK, (27,32),(40,35),2)
    #MOUTH
    pygame.draw.line(image1, COLOR_BLACK, (18,38),(26,38),2)

    #IMAGE2 DRAWING##############################################
    tail_offset_x = 3
    tail_offset_y = 2
    #TAIL
    pygame.draw.line(image2, COLOR_CAT_HEAD, (102,30 + tail_offset_y),(102 - tail_offset_x,0),8)
    leg_offset_x = 3

    #FAR LEGS
    pygame.draw.line(image2, COLOR_CAT_HEAD, (34,50),(34 + leg_offset_x,80),6)
    pygame.draw.line(image2, COLOR_CAT_HEAD, (92,50),(92 - leg_offset_x,80),6)

    #BODY
    pygame.draw.rect(image2, COLOR_CAT_BODY, (32,31,82,24))
    #NEAR LEGS
    pygame.draw.line(image2, COLOR_CAT_HEAD, (44,50),(44 - leg_offset_x,80),6)
    pygame.draw.line(image2, COLOR_CAT_HEAD, (101,50),(101 + leg_offset_x,80),6)

    head_offset = 3
    #HEAD
    pygame.draw.circle(image2, COLOR_CAT_HEAD, (22 + head_offset,30), 22)
    #EARS
    pygame.draw.polygon(image2, COLOR_CAT_HEAD, ((2 + head_offset,20),(7 + head_offset,17),(3 + head_offset,5)))
    pygame.draw.polygon(image2, COLOR_CAT_BODY, ((12 + head_offset,10),(7 + head_offset,17),(3 + head_offset,5)))

    pygame.draw.polygon(image2, COLOR_CAT_HEAD, ((37 + head_offset,15),(43 + head_offset,6),(43 + head_offset,23)))
    pygame.draw.polygon(image2, COLOR_CAT_BODY, ((37 + head_offset,15),(43 + head_offset,6),(35 + head_offset,11)))
    #NOSE
    pygame.draw.circle(image2, COLOR_BLACK, (22 + head_offset,26), 4)
    pygame.draw.circle(image2, COLOR_BLACK, (17 + head_offset,30), 6, 2)
    pygame.draw.circle(image2, COLOR_BLACK, (27 + head_offset,30), 6, 2)
    #EYES
    pygame.draw.circle(image2, COLOR_BLACK, (14 + head_offset,20), 3)
    pygame.draw.circle(image2, COLOR_BLACK, (30 + head_offset,20), 3)    
    #MOUSTACHE
    pygame.draw.line(image2, COLOR_BLACK, (17 + head_offset,28),(4 + head_offset,25),2)
    pygame.draw.line(image2, COLOR_BLACK, (15 + head_offset,30),(2 + head_offset,30),2)
    pygame.draw.line(image2, COLOR_BLACK, (17 + head_offset,32),(4 + head_offset,35),2)


    pygame.draw.line(image2, COLOR_BLACK, (27 + head_offset,28),(40 + head_offset,25),2)
    pygame.draw.line(image2, COLOR_BLACK, (29 + head_offset,30),(42 + head_offset,30),2)
    pygame.draw.line(image2, COLOR_BLACK, (27 + head_offset,32),(40 + head_offset,35),2)
    #MOUTH
    pygame.draw.line(image2, COLOR_BLACK, (18 + head_offset,38),(26 + head_offset,38),2)

    #IMAGE3 DRAWING##############################################
    tail_offset_x = 2
    tail_offset_y = 2
    #TAIL
    pygame.draw.line(image3, COLOR_CAT_HEAD, (102,30 + tail_offset_y),(102 + tail_offset_x,0),8)
    leg_offset_x = -3

    #FAR LEGS
    pygame.draw.line(image3, COLOR_CAT_HEAD, (34,50),(34 + leg_offset_x,80),6)
    pygame.draw.line(image3, COLOR_CAT_HEAD, (92,50),(92 - leg_offset_x,80),6)

    #BODY
    pygame.draw.rect(image3, COLOR_CAT_BODY, (32,31,82,24))
    #NEAR LEGS
    pygame.draw.line(image3, COLOR_CAT_HEAD, (44,50),(44 - leg_offset_x,80),6)
    pygame.draw.line(image3, COLOR_CAT_HEAD, (101,50),(101 + leg_offset_x,80),6)

    head_offset = 1
    #HEAD
    pygame.draw.circle(image3, COLOR_CAT_HEAD, (22 + head_offset,30), 22)
    #EARS
    pygame.draw.polygon(image3, COLOR_CAT_HEAD, ((2 + head_offset,20),(7 + head_offset,17),(3 + head_offset,5)))
    pygame.draw.polygon(image3, COLOR_CAT_BODY, ((12 + head_offset,10),(7 + head_offset,17),(3 + head_offset,5)))

    pygame.draw.polygon(image3, COLOR_CAT_HEAD, ((37 + head_offset,15),(43 + head_offset,6),(43 + head_offset,23)))
    pygame.draw.polygon(image3, COLOR_CAT_BODY, ((37 + head_offset,15),(43 + head_offset,6),(35 + head_offset,11)))
    #NOSE
    pygame.draw.circle(image3, COLOR_BLACK, (22 + head_offset,26), 4)
    pygame.draw.circle(image3, COLOR_BLACK, (17 + head_offset,30), 6, 2)
    pygame.draw.circle(image3, COLOR_BLACK, (27 + head_offset,30), 6, 2)
    #EYES
    pygame.draw.circle(image3, COLOR_BLACK, (14 + head_offset,20), 3)
    pygame.draw.circle(image3, COLOR_BLACK, (30 + head_offset,20), 3)    
    #MOUSTACHE
    pygame.draw.line(image3, COLOR_BLACK, (17 + head_offset,28),(4 + head_offset,25),2)
    pygame.draw.line(image3, COLOR_BLACK, (15 + head_offset,30),(2 + head_offset,30),2)
    pygame.draw.line(image3, COLOR_BLACK, (17 + head_offset,32),(4 + head_offset,35),2)


    pygame.draw.line(image3, COLOR_BLACK, (27 + head_offset,28),(40 + head_offset,25),2)
    pygame.draw.line(image3, COLOR_BLACK, (29 + head_offset,30),(42 + head_offset,30),2)
    pygame.draw.line(image3, COLOR_BLACK, (27 + head_offset,32),(40 + head_offset,35),2)
    #MOUTH
    pygame.draw.line(image3, COLOR_BLACK, (18 + head_offset,38),(26 + head_offset,38),2)

    
    #w, h = CAT_SIZE
    #pygame.draw.rect(image1, COLOR_BLUE, (0,0,w,h),2)
    #pygame.draw.rect(image2, COLOR_RED, (0,0,w,h),2)
    return image1, image2, image1, image3


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.offset_x = CAT_SIZE[0]
        self.imageL = get_cat_images()
        image_list = []
        for image in self.imageL:
            image_list.append(pygame.transform.flip(image, True, False))
        self.imageR = tuple(image_list)
        self.left_position = random.randint(0,1)



        if self.left_position:
            self.x = RESOLUTION[0]
            self.speed_x = -2
            self.image_list = self.imageL
        else:
            self.x = -self.offset_x
            self.speed_x = 2
            self.image_list = self.imageR

        self.counter_animation = 0
        self.counter_animation_max = ANIMATION_DIVIDER//2
        self.number_images = len(self.image_list)
        self.index_image = 0
        self.image = self.image_list[self.index_image]
        self.y = TUPLE_Y_LEVELS[0] - CAT_SIZE[1]//2
        self.eat = False
    

        self.rect = pygame.Rect(pygame.Surface.get_rect(self.image))
        self.rect.center = self.x, self.y

        self.shadow_size = self.rect.w, self.rect.h//4#CAT_BODY_RECT[2:]
        self.meow = pygame.mixer.Sound(file_meow)
        pygame.mixer.Sound.play(self.meow)


    def update(self):
        if not self.alive():
            del self
            return
        self.update_image()
        self.rect.move_ip(self.speed_x, 0)
        self.x, self.y = self.rect.center
        if self.speed_x > 0:
            if self.rect.x > RESOLUTION[0] + self.offset_x:
                if self.cat_has_left():
                    self.kill()
                    del self
                    return
                self.image_list = self.imageL
                self.speed_x *= -1

        else:
            if self.rect.x < - self.offset_x:
                if self.cat_has_left():
                    self.kill()
                    del self
                    return
                self.image_list = self.imageR
                self.speed_x *= -1

    def cat_has_left(self):
        if not random.randint(1,3) % 3:
            return True
        else:
            return False

    def update_image(self):
        if not self.eat:
            if self.counter_animation > self.counter_animation_max:
                self.counter_animation = 0
                self.index_image +=1
                if self.index_image >= self.number_images:
                    self.index_image = 0
            self.counter_animation += 1
            self.image = self.image_list[self.index_image]   




