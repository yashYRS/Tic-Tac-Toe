def get_moves_left(ttt_board):
    return [i for i, val in enumerate(ttt_board) if val == 9]


def check_win(board):
    # checking horizontal :
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == 0:
            return -1
        elif board[i] == board[i+1] == board[i+2] == 1:
            return 1
    # checking diagonal :
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 0:
            return -1
        elif board[i] == board[i+3] == board[i+6] == 1:
            return 1
    # checking diagonal :
    if board[0] == board[8] == board[4] == 0 or board[2] == board[6] == board[4] == 0:
        return -1
    elif board[0] == board[8] == board[4] == 1 or board[2] == board[6] == board[4] == 1:
        return 1
    if len(get_moves_left(board)) > 0:
        return 2
    # draw
    return 0
# +1 for x-win, -1 for o win, 0 for draw, 2 for unfinished


def printer(board):
    a = 0
    for i in board:
        print(i, end=" ")
        a = a+1
        if a % 3 == 0:
            print("")
