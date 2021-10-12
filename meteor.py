import pygame
import random
from constants import gamec


METEOR_GREY_MED_1_PNG = 'assets/meteorGrey_med1.png'
SPEED_LOW = 1
SPEED_FAST = 10
SPEED_X = 5


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(METEOR_GREY_MED_1_PNG).convert()
        self.image.set_colorkey(gamec.BLACK)
        self.rect = self.image.get_rect()
        self.__put_meteor()
        self.speed_x = random.randrange(-SPEED_X, SPEED_X)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if (self.rect.top > gamec.SCREEN_HEIGHT + 10
                or self.rect.left < -25
                or self.rect.right > gamec.SCREEN_WIDTH + 25):
            self.__put_meteor()

    def __put_meteor(self):
        self.rect.x = random.randrange(gamec.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(SPEED_LOW, SPEED_FAST)

