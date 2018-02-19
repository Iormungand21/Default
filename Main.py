import pygame
import os
import time
import pygame.transform
import random
import GlobalVars
from Entity import Entity, entity_list
from GameFunctions import key_update, update_all, text_objects
from Player import Player
pygame.init()

display_width = GlobalVars.display_width
display_height = GlobalVars.display_height

black = GlobalVars.black
white = GlobalVars.white
red = GlobalVars.red
blue = GlobalVars.blue
green = GlobalVars.green

speed_decay = GlobalVars.speed_decay
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GAME TIME')
clock = pygame.time.Clock()
up_down_left_right = GlobalVars.up_down_left_right


class Block(Entity):
    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(5)
    game_reset()
    game_loop()


def game_over(player):
    if player.player_collison_check() or player.player_bounds_check():
        crash()


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
        player_ship.display_entity(gameDisplay)
        guns.display_entity(player_ship.image)
        death_block.create_rect(black, gameDisplay)
        death_block.block_move()
        game_over(player_ship)
        death_block.block_reset()
        update_all(entity_list)
        pygame.display.update()

        clock.tick(60)


player_ship = Player('ship', (display_width * 0.45), (display_height * 0.8), 10,
                     pygame.image.load_extended(os.path.join("Ship2.png")), acceleration=1)

guns = Entity('guns', player_ship.x, player_ship.y, 0, pygame.image.load_extended(os.path.join("gun1.png")))

death_block = Entity('block', random.randrange(0, display_width), -600, 7, image=None, width=100, height=100)

game_loop()
pygame.quit()
quit()
