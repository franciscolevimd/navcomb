import pygame

from constants import gamec


class Game():
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

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
        screen.fill(gamec.BLACK)
        self.all_sprites.draw(screen)
        pygame.display.flip()