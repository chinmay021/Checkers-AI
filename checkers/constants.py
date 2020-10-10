import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
LIGHT_BLUE = (72, 193, 235)

CROWN = pygame.transform.scale(pygame.image.load(
    'checkers/assets/crown.png'), (45, 25))
