import random

import pygame
import GlobalVars

display_width = GlobalVars.display_width
display_height = GlobalVars.display_height
entities_friendly = []
entities_enemies = []
entities_friendly_bullets = []
entity_list = [entities_friendly, entities_enemies, entities_friendly_bullets]


class Entity:
    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0, alive=True):
        super().__init__()
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
        self.alive = alive
        if image:
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        self.xmax = x + self.width
        self.ymax = y + self.height

    def display_entity(self, game_display):
        if self.alive:
            if self.image:
                game_display.blit(self.image, (self.x, self.y))
            self.xmax = self.x + self.width
            self.ymax = self.y + self.height

    def entity_collision(self, ent_list):
        for entity in ent_list:
            if (self.x < entity.xmax and self.y < entity.ymax) and (self.xmax > entity.x and
                                                                    self.ymax > entity.y) and entity.alive:
                if self.name is not entity.name:
                    return True, entity


class Background(Entity):

    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)
        self.start_y = y

    def move(self):
        self.y += self.speed

    def reset(self):
        if self.y == display_height:
            self.y = -1000
