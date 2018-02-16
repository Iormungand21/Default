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
    def __init__(self, name, x, y, speed, image=None, width=0, height=0):
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.width = width
        self.height = height
        if image:
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        self.xmax = x + self.width
        self.ymax = y + self.height
        entity_list.append(self)

    def display_entity(self):
        if self.image:
            gameDisplay.blit(self.image, (self.x, self.y))

    def create_rect(self, color):
        pygame.draw.rect(gameDisplay, color, [self.x, self.y, self.width, self.height])

    def block_reset(self):
        if self.y > display_height + self.height:
            self.y = 0 - self.height
            self.x = random.randrange(0, display_width)

    def block_move(self):
        self.y += self.speed

    def entity_colission(self, ent_list):
        print('ok')
        for entity in ent_list:
            print(entity.name)
            if (self.x < entity.xmax and self.y < entity.ymax) and (self.xmax > entity.x and self.ymax > entity.y):
                if self.name is not entity.name:
                    crash()




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
        print('ok')
        if self.x > display_width - self.width or self.x < 0 or self.y > display_height - self.height or self.y < 0:
            crash()





player_ship = Player('ship', (display_width * 0.45), (display_height * 0.8), 5,
                     pygame.image.load_extended(os.path.join("Ship.png")))
death_block = Entity('block', random.randrange(0, display_width), -600, 7, image=None, width=100, height=100)

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
        death_block.create_rect(black)

        death_block.block_move()
        death_block.block_reset()
        player_ship.player_bounds_check()
        player_ship.entity_colission(entity_list)

        x_max = x + ship_width
        y_max = y + ship_height
        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()
