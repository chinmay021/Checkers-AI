from minimax.algorithm import minimax
# from checkers.piece import Piece
import pygame
from checkers.constants import GREEN, SQUARE_SIZE, WIDTH, HEIGHT, RED, BLACK
from checkers.game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()

    game = Game(WIN)

    # piece = board.get_piece(0, 1)
    # board.move(piece, 4, 3)
    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            new_board = minimax(game.get_board(), 3, True, game)[1]
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col, WIN)
        game.update()

    pygame.quit()


main()
