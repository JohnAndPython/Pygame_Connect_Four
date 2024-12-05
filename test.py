
board = []

for _ in range(6):
    board.append(7 * [0])


def whatever(ind):
    for value in board:
        if value[ind] == 0:
             return True
        
    return False


def set_value(index, value) -> None:

    for ind, row in enumerate(board):
        if row[index] == 0 and ind == 5:
            board[ind][index] = value
        elif row[index] != 0:
            board[ind-1][index] = value


board[5][4] = 1


print(board)





set_value(4, 1)

print(board)