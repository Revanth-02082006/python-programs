board = [" " for _ in range(9)]

def display_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

display_board()
