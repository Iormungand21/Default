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

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GAME TIME')
clock = pygame.time.Clock()
entity_list = []
shipImg = pygame.image.load_extended(os.path.join("Ship.png"))


class Entity:
    def __init__(self, name, x, y, speed, image=None):
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.xmax = x + self.width
        self.ymax = y + self.height
        entity_list.append(self)

    def display_entity(self):
        gameDisplay.blit(self.image, (self.x, self.y))
        size = self.image.get_size()
    def entity_colission(self):
        return



class Player(Entity):
    def control_check_up(self, event, x_change, y_change):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = self.speed * -1
            elif event.key == pygame.K_RIGHT:
                x_change = self.speed
            elif event.key == pygame.K_DOWN:
                y_change = self.speed
            elif event.key == pygame.K_UP:
                y_change = self.speed * -1
        return x_change, y_change

    def control_check_down(self, event, x_change, y_change):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and x_change == self.speed * -1:
                x_change = 0
            elif event.key == pygame.K_RIGHT and x_change == self.speed:
                x_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
        return x_change, y_change

    def player_bounds_check(self):
        if self.x > display_width - self.width or self.x < 0 or self.y > display_height - self.height or self.y < 0:
            crash()

    def player_collision_check(self, entity):
        if (x < thingx_max and y < thingy_max) and (x_max > thingx and y_max > thingy):
            crash()



player_ship = Player('ship', (display_width * 0.45), (display_height * 0.8), 5,
                     pygame.image.load_extended(os.path.join("Ship.png")))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def ship(x, y):
    gameDisplay.blit(shipImg, (x, y))


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
    game_loop()


def crash():
    message_display('You crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    ship_width = 32
    ship_height = 32
    player_delta = []

    thingx = random.randrange(0, display_width)
    thingy = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    thingx_max = thingx + thing_width
    thingy_max = thingy + thing_height

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            player_delta = player_ship.control_check_up(event, x_change, y_change)
            player_delta = player_ship.control_check_down(event, player_delta[0], player_delta[1])

        player_ship.y += player_delta[1]
        player_ship.x += player_delta[0]
        gameDisplay.fill(white)
        player_ship.display_entity()

        things(thingx, thingy, thing_width, thing_height, black)
        thingy += thing_speed

        player_ship.player_bounds_check()

        if thingy > display_height + thing_height:
            thingy = 0 - thing_height
            thingx = random.randrange(0, display_width)

        x_max = x + ship_width
        y_max = y + ship_height
        thingx_max = thingx + thing_width
        thingy_max = thingy + thing_height

        if (x < thingx_max and y < thingy_max) and (x_max > thingx and y_max > thingy):
            #print('crash')
            #print('x = ' + str(x) + ' xmax = ' + str(x_max))
            #print('y = ' + str(y) + ' ymax = ' + str(y_max))
            #print('blockx = ' + str(thingx) + ' bloacky = ' + str(thingy))
            #print('blockymax = ' + str(thingx_max) + ' bloacky = ' + str(thingy_max))

            crash()
        print(entity_list)
        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()
