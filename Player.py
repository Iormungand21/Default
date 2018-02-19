import GlobalVars
from Entity import Entity, entity_list


class Player(Entity):
    def __init__(self, name, x, y, speed, image=None, width=0, height=0, acceleration=0):
        super().__init__(name, x, y, speed, image, width, height, acceleration)

    def player_movement(self, keys):
        if self.speed - 1 >= self.xchange >= ((self.speed - 1) * -1):
            if keys[2]:
                self.xchange += (self.accel * -1)
            elif keys[3]:
                self.xchange += self.accel

        if self.speed - 1 >= self.ychange >= ((self.speed - 1) * -1):
            if keys[0]:
                self.ychange += (self.accel * -1)
            elif keys[1]:
                self.ychange += self.accel

        if self.xchange != 0:
            if not keys[2] and self.xchange < 0:
                self.xchange += GlobalVars.speed_decay
            elif not keys[3] and self.xchange > 0:
                self.xchange += GlobalVars.speed_decay * -1

        if self.ychange != 0:
            if not keys[0] and self.ychange < 0:
                self.ychange += GlobalVars.speed_decay
            elif not keys[1] and self.ychange > 0:
                self.ychange += GlobalVars.speed_decay * - 1
        self.x += self.xchange
        self.y += self.ychange

        print("x " + str(self.xchange))
        print("y " + str(self.ychange))

    def player_bounds_check(self):
        if (self.x > GlobalVars.display_width - self.width or
                self.x < 0 or self.y > GlobalVars.display_height - self.height or self.y < 0):
            return True
        else:
            return False

    def player_collison_check(self):
        collided = self.entity_collision(entity_list[1])
        if collided:
            return True
        else:
            return False
