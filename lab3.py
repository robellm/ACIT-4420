import random

rows = int(input("What is the size in horizontal direction? "))
columns = int(input("What is the size in vertical direction? "))
mines = int(input("How many mines should we have? "))

SizeX = rows
SizeY = columns
board = [[0] * SizeY for i in range(SizeX)]
mask = [[0] * SizeY for i in range(SizeX)]

for i in range(mines):
    x = -1
    y = -1
    while x == -1 or board[x][y] == 9:
        x = random.randint(0, SizeX-1)
        y = random.randint(0, SizeY-1)
    board[x][y] = 9

for i in range(SizeX):
    for j in range(SizeY):
        if board[i][j] != 9:
            if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == 9 : board[i][j] += 1
            if i-1 >= 0 and board[i-1][j] == 9 : board[i][j] += 1
            if i-1 >= 0 and j < SizeY -1 and board[i-1][j+1] == 9: board[i][j] += 1
            if j-1 >= 0 and board[i][j-1] == 9 : board[i][j] += 1
            if j < SizeY-1 and board[i][j+1] == 9 : board[i][j] += 1
            if i < SizeX-1 and j-1 >= 0 and board[i+1][j-1] == 9 : board[i][j] += 1
            if i < SizeX-1 and board[i+1][j] == 9 : board[i][j] += 1
            if i < SizeX-1 and j < SizeY-1 and board[i+1][j+1] == 9 : board[i][j] += 1


def print_board():
    for i in range(SizeY):
        s = ' '
        for j in range(SizeX):
            if mask[i][j] == 1:
                if board[i][j] == 9:
                    s += '*'
                else:
                    s += str(board[i][j])
            else:
                s += '?'
        print(s)


def Winning_condition():
    for i in range(SizeX):
        s = ''
        for j in range(SizeY):
            if board[i][j] == 9:
                s += '*'
            else:
                s += str(board[i][j])
        print(s)


ended = False
while not ended:
    print_board()
    s = input("Your shot:")
    if s != 'x':
        guessx = int(s.split()[0])-1
        guessy = int(s.split()[1])-1

        mask[guessx][guessy] = 1

        if board[guessx][guessy] == 9:
            Winning_condition()
            print('You lost!')
            ended = True
        check=True
        for i in range(SizeX):
            for j in range(SizeX):
                if mask[i][j] == 0 and board[i][j] != 9:
                    check=False
        if check:
            Winning_condition()
            print('You win!')
            ended= True
    else:
        ended = True
