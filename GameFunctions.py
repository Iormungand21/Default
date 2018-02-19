import pygame

from GlobalVars import up_down_left_right, black


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


def update_all(ent_list):
    for entity in ent_list:
        entity.xmax = entity.x + entity.width
        entity.ymax = entity.y + entity.height


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

