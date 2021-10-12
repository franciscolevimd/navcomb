import pygame

from constants import gamec


SHIP_SPRITE_NAME = 'assets/ship.png'


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(SHIP_SPRITE_NAME).convert()
        self.image.set_colorkey(gamec.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = gamec.SCREEN_WIDTH // 2
        self.rect.bottom = gamec.SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -gamec.SHIP_SPEED
        if key_state[pygame.K_RIGHT]:
            self.speed_x = gamec.SHIP_SPEED
        self.rect.x += self.speed_x
        if self.rect.right > gamec.SCREEN_WIDTH:
            self.rect.right = gamec.SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
