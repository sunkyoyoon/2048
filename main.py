import random

def initialize_game():
    game_board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(game_board)
    add_new_tile(game_board)
    return game_board

def add_new_tile(game_board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if game_board[i][j] == 0]
    if not empty_tiles:
        return
    i, j = random.choice(empty_tiles)
    game_board[i][j] = random.choice([2, 4])

def compress_board(board):
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge_tiles(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse_board(board):
    return [row[::-1] for row in board]

def transpose_board(board):
    return [list(row) for row in zip(*board)]

def move_left(game_board):
    game_board = compress_board(game_board)
    game_board = merge_tiles(game_board)
    game_board = compress_board(game_board)
    return game_board

def move_right(game_board):
    game_board = reverse_board(game_board)
    game_board = move_left(game_board)
    game_board = reverse_board(game_board)
    return game_board

def move_up(game_board):
    game_board = transpose_board(game_board)
    game_board = move_left(game_board)
    game_board = transpose_board(game_board)
    return game_board

def move_down(game_board):
    game_board = transpose_board(game_board)
    game_board = move_right(game_board)
    game_board = transpose_board(game_board)
    return game_board

def print_board(game_board):
    for row in game_board:
        print(' '.join([str(cell).ljust(4) for cell in row]))
    print()

def get_user_move():
    moves = {'w': move_up, 's': move_down, 'a': move_left, 'd': move_right}
    while True:
        move = input("Enter move (W/A/S/D): ").lower()
        if move in moves:
            return moves[move]

def main():
    game_board = initialize_game()
    while True:
        print_board(game_board)
        move_func = get_user_move()
        game_board = move_func(game_board)
        add_new_tile(game_board)
        # You can add a check here to see if the game is over

if __name__ == "__main__":
    main()