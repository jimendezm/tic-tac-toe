import pygame
import sys
from minimax import ai_play
from utils import players, terminal, utility, PLAYER_X, PLAYER_O

pygame.init()

WIDTH, HEIGHT = 600, 700
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Minimax")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)

font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 30)

board = [[None for _ in range(3)] for _ in range(3)]

game_over = False

button_rect = pygame.Rect(200, 620, 200, 50)

def draw_board():
    screen.fill(WHITE)

    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 3)

            if board[i][j] is not None:
                text = font.render(board[i][j], True, BLACK)
                screen.blit(text, (j*CELL_SIZE+60, i*CELL_SIZE+40))

    pygame.draw.rect(screen, GRAY, button_rect)
    text = small_font.render("Reiniciar", True, BLACK)
    screen.blit(text, (button_rect.x+50, button_rect.y+15))

    if game_over:
        result_text = ""
        u = utility(board)
        if u == 1:
            result_text = "Gana X"
        elif u == -1:
            result_text = "Gana O"
        else:
            result_text = "Empate"

        label = small_font.render(result_text, True, BLACK)
        screen.blit(label, (250, 580))

def get_cell(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

def main():
    global board, game_over

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_rect.collidepoint(event.pos):
                    board = [[None for _ in range(3)] for _ in range(3)]
                    game_over = False
                    continue

                if not game_over:
                    row, col = get_cell(event.pos)

                    if board[row][col] is None:
                        board[row][col] = PLAYER_X

                        if terminal(board):
                            game_over = True
                        else:
                            move = ai_play(board)
                            if move:
                                x, y = move
                                board[y][x] = PLAYER_O

                            if terminal(board):
                                game_over = True

        draw_board()
        pygame.display.flip()
        clock.tick(60)

main()
