import pygame

from ship import Ship
from meteor import Meteor


BACKGROUND_PNG = 'assets/background.png'


class Game():
    def __init__(self):
        self.background = pygame.image.load(BACKGROUND_PNG).convert()
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.ship = Ship()
        self.all_sprites.add(self.ship)
        for i in range(8):
            meteor = Meteor()
            self.all_sprites.add(meteor)
            self.meteors.add(meteor)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
                return False
        return True

    def run_logic(self):
        self.all_sprites.update()

    def display_frame(self, screen):
        screen.blit(self.background, [0, 0])
        self.all_sprites.draw(screen)
        pygame.display.flip()
