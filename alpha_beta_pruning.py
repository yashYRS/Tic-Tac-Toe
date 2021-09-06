import utils


def abprune(board, depth, Max, alpha, beta):
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
            val = abprune(board, depth+1, False, alpha, beta)
            best = max(best, val)
            board[move] = 9
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 99
        for move in moves:
            board[move] = 0
            val = abprune(board, depth+1, True, alpha, beta)
            best = min(best, val)
            board[move] = 9
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def best_move(board):
    # worst case -- loss
    best_move = -1
    score = -1
    alpha, beta = -99, 99
    moves = utils.get_moves_left(board)
    for move in moves:
        board[move] = 1
        current_score = abprune(board, 0, False, alpha, beta)
        if (current_score >= score):
            best_move = move
            score = current_score
        board[move] = 9
    return best_move
