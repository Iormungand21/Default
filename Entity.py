import random

import pygame
import GlobalVars

display_width = GlobalVars.display_width
display_height = GlobalVars.display_height
entity_list = []


class Entity:

    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.width = width
        self.height = height
        self.accel = acceleration
        self.xchange = 0
        self.ychange = 0
        if image:
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        self.xmax = x + self.width
        self.ymax = y + self.height
        entity_list.append(self)

    def display_entity(self, game_display):
        if self.image:
            game_display.blit(self.image, (self.x, self.y))
        self.xmax = self.x + self.width
        self.ymax = self.y + self.height

    def create_rect(self, color, game_display):
        pygame.draw.rect(game_display, color, [self.x, self.y, self.width, self.height])
        self.xmax = self.x + self.width
        self.ymax = self.y + self.height

    def block_reset(self):
        if self.y > display_height + self.height:
            self.y = 0 - self.height
            self.x = random.randrange(0, display_width)

    def block_move(self):
        self.y += self.speed

    def entity_collision(self, ent_list):
        for entity in ent_list:
            if (self.x < entity.xmax and self.y < entity.ymax) and (self.xmax > entity.x and self.ymax > entity.y):
                if self.name is not entity.name:
                    return True
