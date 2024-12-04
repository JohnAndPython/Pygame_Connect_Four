
board = []

for _ in range(6):
    lst = board.append(7 * [0])


def whatever(ind):
    for value in board:
        if value[ind] == 0:
             return True
        
    return False


board[0][0] = 1
board[0][1] = 1
board[0][2] = 1
board[0][3] = 1
board[0][4] = 1
board[0][5] = 1
board[0][6] = 1

print(board)


index = 4


print(whatever(index))