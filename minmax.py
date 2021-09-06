import utils


def minimax(board, depth, Max):
    # Max - True for maximizer , False for minimizer
    value_board = utils.check_win(board)
    # printer(board,value_board)
    if value_board != 2:
        return value_board                  # if game-over return winner..
    moves = utils.get_moves_left(board)
    if Max:
        best = -99
        for move in moves:
            board[move] = 1
            val = minimax(board, depth+1, False)
            best = max(best, val)
            board[move] = 9
        return best
    else:
        best = 99
        for move in moves:
            board[move] = 0
            val = minimax(board, depth+1, True)
            best = min(best, val)
            board[move] = 9
        return best


def best_move(board):
    # worst case -- loss
    best_move = -1
    score = -1
    moves = utils.get_moves_left(board)
    for move in moves:
        board[move] = 1
        current_score = minimax(board, 0, False)
        if (current_score >= score):
            best_move = move
            score = current_score
        board[move] = 9
    return best_move
