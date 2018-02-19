import pygame, random
from Entity import Entity, entity_list
from GlobalVars import display_height, display_width


class Block(Entity):
    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)
        entity_list[1].append(self)

    def create_rect(self, color, game_display):
        if self.alive:
            pygame.draw.rect(game_display, color, [self.x, self.y, self.width, self.height])
            self.xmax = self.x + self.width
            self.ymax = self.y + self.height

    def block_reset(self):
        if self.y > display_height + self.height:
            self.y = 0 - self.height
            self.x = random.randrange(0, display_width)

    def block_move(self):
        self.y += self.speed
