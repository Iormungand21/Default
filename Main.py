import pygame
import os
import time
import pygame.transform
import random
import GlobalVars
from Block import Block
from Entity import entity_list, Background
from GameFunctions import key_update, update_all, text_objects, bullet_update, entity_cleanup
from Weapons import Gun
from Player import Player

pygame.init()

display_width = GlobalVars.display_width
display_height = GlobalVars.display_height

images = {
    "ship": pygame.image.load_extended(os.path.join("res", "Ship2.png")),
    "gun": pygame.image.load_extended(os.path.join("res", "gun1.png")),
    "background": pygame.image.load_extended(os.path.join("res", "background.png"))
}

black = GlobalVars.black
white = GlobalVars.white
red = GlobalVars.red
blue = GlobalVars.blue
green = GlobalVars.green

speed_decay = GlobalVars.speed_decay
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GAME TIME')
clock = pygame.time.Clock()
up_down_left_right = GlobalVars.up_down_left_right_fire


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(5)
    game_reset()
    game_loop()


def bullet_hit(ent_list):
    for bullet in ent_list[2]:
        results = bullet.entity_collision(ent_list[1])
        if results:
            bullet.alive = False
            results[1].alive = False
            print(results)


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
        update_all(entity_list)
        player_ship.player_movement(up_down_left_right)
        gameDisplay.fill(white)
        background.reset()
        background2.reset()
        background.display_entity(gameDisplay)
        background2.display_entity(gameDisplay)
        background.move()
        background2.move()
        player_ship.display_entity(gameDisplay)
        death_block.create_rect(black, gameDisplay)
        death_block.block_move()
        game_over(player_ship)
        death_block.block_reset()
        guns.gun_update(player_ship)
        guns.gun_display(gameDisplay)
        guns.gun_fire(player_ship, gameDisplay, up_down_left_right)
        bullet_update(entity_list, gameDisplay)
        update_all(entity_list)
        bullet_hit(entity_list)
        pygame.display.update()
        entity_cleanup(entity_list)
        clock.tick(60)


background = Background('background', 0, 0, 4, image=images['background'])
background2 = Background('background', 0, -1000, 4, image=images['background'])
player_ship = Player('ship', (display_width * 0.45), (display_height * 0.8), 10,
                     images['ship'], acceleration=1)
guns = Gun('guns', player_ship.x, player_ship.y, 0, 5, None, image=images['gun'])
death_block = Block('block', random.randrange(0, display_width), -600, 7, image=None, width=100, height=100)

game_loop()
pygame.quit()
quit()
