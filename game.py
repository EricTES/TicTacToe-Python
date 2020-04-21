from copy import deepcopy
import random

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


def print_board(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()


def clear_board(board):
    new_line = ["-", "-", "-"]
    for i in range(3):
        board[i] = list(new_line)


def get_remaining_cells(board):
    remaining_cells = []
    for row in range(board.__len__()):
        for column in range(board[row].__len__()):
            if board[row][column] != "X" and board[row][column] != "O":
                remaining_cells.append((row, column))
    return remaining_cells


def has_won(board, player):
    # Horizontal check
    for row in board:
        if row.count(player) == 3:
            return True
    # Vertical check
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Diagonal Check
    if board[1][1] == player:
        if (board[0][0] == player and board[2][2] == player) or (board[2][0] == player and board[0][2] == player):
            return True
    return False


def game_ended(board):
    return has_won(board, "X") or has_won(board, "O") or not get_remaining_cells(board)


def evaluate(board):
    if has_won(board, "X"):
        return 1
    elif has_won(board, "O"):
        return -1
    return 0


def minimax(board, is_x):
    if game_ended(board):
        return [evaluate(board), ()]
    best_cell = ""
    if is_x:
        evaluation = -1
        symbol = "X"
    else:
        evaluation = 1
        symbol = "O"

    for row, column in get_remaining_cells(board):
        temp_board = deepcopy(board)
        temp_board[row][column] = symbol
        number = minimax(temp_board, not is_x)[0]
        ran = random.randint(0, 1)
        if is_x and number >= evaluation:
            if evaluation == number and ran == 1:
                best_cell = (row, column)
            else:
                evaluation = number
                best_cell = (row, column)
        elif not is_x and number <= evaluation:
            if evaluation == number and ran == 1:
                best_cell = (row, column)
            else:
                evaluation = number
                best_cell = (row, column)
    return [evaluation, best_cell]


num1 = 1
num2 = 1

print(max(num1, num2))
