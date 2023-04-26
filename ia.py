import random

def ia(board, signe):
    available = [i for i in range(9) if board[i] == 0]
    if not available:
        return False
    i = random.choice(available)
    return i