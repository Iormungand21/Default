import pygame
import time

from Entity import Entity, entity_list
from GlobalVars import display_height, display_width, red


class Gun(Entity):
    def __init__(self, name, x, y, speed, fire_rate, bullet_type, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)
        self.fire_rate = fire_rate
        self.bullet_type = bullet_type
        entity_list[0].append(self)
        self.last_shot = 0

    def gun_display(self, target):
        target.blit(self.image, (self.x, self.y))

    def gun_update(self, target):
        self.x = target.x
        self.y = target.y

    def gun_fire(self, player, game_display, keys, clock):
        gun_time = (pygame.time.get_ticks() / 100)
        if gun_time - self.last_shot > self.fire_rate:
            if keys[4]:
                bullet = Bullet('player_bullet', player.x + (player.width/2) -2, player.y, 20, width=4, height=20)
                pygame.draw.rect(game_display, red, [bullet.x, bullet.y, bullet.width, bullet.height])
                self.last_shot = gun_time


class Bullet(Entity):
    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)
        entity_list[2].append(self)
