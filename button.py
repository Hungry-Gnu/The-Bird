import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, rect, font, font_size, text, passive_color, active_color, text_color, action = None):
        super().__init__()
        self.active_surface = pygame.Surface(rect[2:])
        self.active_surface.fill(active_color)
        self.passive_surface = self.active_surface.copy()
        self.passive_surface.fill(passive_color)
        #self.passive_surface.set_colorkey(passive_color)
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.action = action
        #BLIT TEXT IN BUTTON ACTIVE AND PASSIVE SURFACES
        button_font = pygame.font.SysFont(font, font_size)
        text_surface = button_font.render(text, True, text_color)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = self.active_surface.get_rect().center
        self.active_surface.blit(text_surface, text_rectangle)
        self.passive_surface.blit(text_surface, text_rectangle)
        self.image = self.passive_surface

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_position):

            self.image = self.active_surface
            if mouse_click[0] and (self.action != None):
                self.action()

        else:
            self.image = self.passive_surface

