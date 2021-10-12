import pygame


from constants import gamec
from game import Game


GAME_TITLE = 'NavComb'


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((gamec.SCREEN_WIDTH, gamec.SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    running = True
    clock = pygame.time.Clock()
    game = Game()
    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(gamec.FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
