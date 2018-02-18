import pygame
import os
import time
import pygame.transform
import random


pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

speed_decay = 0.5
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GAME TIME')
clock = pygame.time.Clock()
entity_list = []
key_list = []
up_down_left_right = [False, False, False, False]


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

    def display_entity(self):
        if self.image:
            gameDisplay.blit(self.image, (self.x, self.y))
        self.xmax = self.x + self.width
        self.ymax = self.y + self.height

    def create_rect(self, color):
        pygame.draw.rect(gameDisplay, color, [self.x, self.y, self.width, self.height])
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
                    crash()


class Player(Entity):

    def player_movement(self, keys):
        if self.speed -1 >= self.xchange >= ((self.speed -1) * -1):
            if keys[2]:
                self.xchange += (self.accel * -1)
            elif keys[3]:
                self.xchange += self.accel

        if self.speed -1 >= self.ychange >= ((self.speed -1) * -1):
            if keys[0]:
                self.ychange += (self.accel * -1)
            elif keys[1]:
                self.ychange += self.accel

        if self.xchange != 0:
            if not keys[2] and self.xchange < 0:
                self.xchange += speed_decay
            elif not keys[3] and self.xchange > 0:
                self.xchange += speed_decay * -1

        if self.ychange != 0:
            if not keys[0] and self.ychange < 0:
                self.ychange += speed_decay
            elif not keys[1] and self.ychange > 0:
                self.ychange += speed_decay * -1
        self.x += self.xchange
        self.y += self.ychange

        print("x " + str(self.xchange))
        print("y " + str(self.ychange))

    def player_bounds_check(self):
        if self.x > display_width - self.width or self.x < 0 or self.y > display_height - self.height or self.y < 0:
            crash()


def key_update(events):
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                up_down_left_right[2] = True

            elif events.key == pygame.K_RIGHT:
                up_down_left_right[3] = True

            elif events.key == pygame.K_DOWN:
                up_down_left_right[1] = True

            elif events.key == pygame.K_UP:
                up_down_left_right[0] = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT:
                up_down_left_right[2] = False

            elif events.key == pygame.K_RIGHT:
                up_down_left_right[3] = False

            elif events.key == pygame.K_DOWN:
                up_down_left_right[1] = False

            elif events.key == pygame.K_UP:
                up_down_left_right[0] = False


def update_all(list):
    for entity in list:
        entity.xmax = entity.x + entity.width
        entity.ymax = entity.y + entity.height


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(5)
    game_reset()
    game_loop()


def crash():
    message_display('You crashed')


def game_reset():
    death_block.y = 0 - death_block.height
    death_block.x = random.randrange(0, display_width)
    player_ship.x = (display_width * 0.45)
    player_ship.y = (display_height * 0.8)
    up_down_left_right[0] = False
    up_down_left_right[1] = False
    up_down_left_right[2] = False
    up_down_left_right[3] = False


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            key_update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        player_ship.player_movement(up_down_left_right)
        gameDisplay.fill(white)
        player_ship.display_entity()

        death_block.create_rect(black)
        death_block.block_move()
        player_ship.player_bounds_check()
        player_ship.entity_collision(entity_list)
        death_block.block_reset()

        update_all(entity_list)
        pygame.display.update()

        clock.tick(60)


player_ship = Player('ship', (display_width * 0.45), (display_height * 0.8), 10,
                     pygame.image.load_extended(os.path.join("Ship.png")), acceleration=1)

death_block = Entity('block', random.randrange(0, display_width), -600, 7, image=None, width=100, height=100)
game_loop()
pygame.quit()
quit()
