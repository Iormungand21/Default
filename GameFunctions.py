import pygame

from GlobalVars import up_down_left_right_fire, black, red


def key_update(events):
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_LEFT:
            up_down_left_right_fire[2] = True
        elif events.key == pygame.K_RIGHT:
            up_down_left_right_fire[3] = True
        elif events.key == pygame.K_DOWN:
            up_down_left_right_fire[1] = True
        elif events.key == pygame.K_UP:
            up_down_left_right_fire[0] = True
        elif events.key == pygame.K_SPACE:
            up_down_left_right_fire[4] = True

    if events.type == pygame.KEYUP:
        if events.key == pygame.K_LEFT:
            up_down_left_right_fire[2] = False
        elif events.key == pygame.K_RIGHT:
            up_down_left_right_fire[3] = False
        elif events.key == pygame.K_DOWN:
            up_down_left_right_fire[1] = False
        elif events.key == pygame.K_UP:
            up_down_left_right_fire[0] = False
        elif events.key == pygame.K_SPACE:
            up_down_left_right_fire[4] = False


def update_all(ent_list):
    for entity_list in ent_list:
        for entity in entity_list:
            entity.xmax = entity.x + entity.width
            entity.ymax = entity.y + entity.height


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def bullet_update(entity_list, game_display):
    for entity in entity_list[2]:
        if entity.alive:
            entity.y += entity.speed * - 1
            pygame.draw.rect(game_display, red, [entity.x, entity.y, entity.width, entity.height])


def entity_cleanup(entity_list):
    for ent_list in entity_list:
        for entity in ent_list:
            if not entity.alive:
                ent_list.remove(entity)
