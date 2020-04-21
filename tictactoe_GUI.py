import pygame
from game import *

# Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 123, 0)

pygame.init()
screen = pygame.display.set_mode((500, 600), 0, 32)
screen.fill(WHITE)
pygame.display.set_caption('Tic Tac Toe')

selected = None
player = None
gameover = False
end_game_text = ""


def draw_board():
    board_width = 400
    board_height = 400
    margin = board_width // 3
    offset = 50
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (offset, margin * i), (500 - offset, margin * i), 3)
        pygame.draw.line(screen, BLACK, ((margin * i) + offset, 0), ((margin * i) + offset, board_height), 3)

    font = pygame.font.SysFont("comicsansms", 72)

    x_origin = offset
    y_origin = 0
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell != "-":
                text = font.render(cell, True, BLACK)
                screen.blit(text, (x_origin + 39 + (i * margin), y_origin + (j * margin)))
    if selected:
        row, col = selected
        pygame.draw.rect(screen, RED, (x_origin +(margin * row), y_origin +(margin * col), margin, margin), 3)


def place(symbol):
    global selected
    global player
    if player is None:
        player = symbol

    if selected and board[selected[0]][selected[1]] == "-" and not gameover:
        row, column = selected
        board[row][column] = symbol
        selected = None

def cpu_move():
    is_maximizing = False if player == "X" else True
    computer_symbol = "O" if player == "X" else "X"
    evaluation, cpu_moves = minimax(board, is_maximizing)
    if len(cpu_moves) > 0:
        cpu_row = cpu_moves[0]
        cpu_col = cpu_moves[1]
        print("Cpu move: {}".format(computer_symbol))
        board[cpu_row][cpu_col] = computer_symbol

def end_of_game(evaluation):
    global end_game_text
    global gameover

    if evaluation == 1:
        end_game_text = "X wins"
    elif evaluation == -1:
        end_game_text = "O wins"
    else:
        end_game_text = "TIE"

    gameover = True


def select(pos):
    global selected

    if 50 < pos[0] < 450 and 0 < pos[1] < 400 and not gameover:
        margin = 400 // 3
        column = pos[1] // margin
        row = (pos[0] - 50) // margin
        print(board[row][column] == '-')
        if board[row][column] == '-':
            selected = (row, column)
            print(selected)


def new_game():
    global gameover
    global end_game_text
    global selected
    global player
    gameover = False
    end_game_text = ""
    selected = None
    player = None
    clear_board(board)
    print("here")


def redraw_board():
    global end_game_text
    screen.fill(WHITE)
    draw_board()

    pygame.draw.rect(screen, ORANGE, (500 // 2 - 55, 510, 110, 50))
    font = pygame.font.SysFont("comicsans", 28)
    text = font.render("New Game", 1, BLACK)
    screen.blit(text, (500 // 2 - 50, 530))

    if gameover:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render(end_game_text, 1, RED)
        screen.blit(text, (400 // 2, 400 // 2 - 20))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if 195 <= mouse_position[0] <= 305 and 510 <= mouse_position[1] <= 560:
                new_game()
            else:
                select(mouse_position)
        if event.type == pygame.KEYDOWN:
            if 120 == event.key or 111 == event.key:
                symbol = event.unicode.upper()
                if player is None or symbol == player :
                    place(symbol)
                    cpu_move()
                    if game_ended(board):
                        end_of_game(evaluate(board))
        redraw_board()
    pygame.display.update()
