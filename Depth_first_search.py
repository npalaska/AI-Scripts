import copy
import sys

##Global Variables
completeboard = {}
open_list = []
closed_list = []
COLUMN = 0
ROW = 4

# Create a trangular solitaire board with one empty slot anywhere as per our requrement.
# The board will look like as follows where F represent filled position and O represent empty position.
"""
        F
      F F
    F O F
  F F F F
F F F F F
"""

def fullboard(board):
    ROW = 4
    COLUMN = 0
    iteration = 0
    #board = ([])
    while ROW <= 4 and ROW >= 0:
        while COLUMN >= 0 and COLUMN <= 4:
            board[COLUMN, ROW] = 'F'
            COLUMN += 1
        COLUMN = 0
        while COLUMN < iteration:
            board[COLUMN, ROW] = ' '
            COLUMN += 1
        ROW -= 1
        iteration+=1
        COLUMN = iteration
    board[3, 2] = 'O'
    print(board)
    return board


# Check the valid mocves where the marbles can move i.e all the possible diagonals with either direction.
def validmove(board):
    print(open_list)
    count = 0
    for i in board:
        if board[i] == 'F':
            count += 1
    if count == 1:
        output = open('result.txt', 'w')
        string = str(open_list)
        newstring = string.replace(" {", "\n\n{")
        output.write(newstring + "\n")
        sys.exit("got the solution")

    else:
        for i in board:
            if board[i] == 'F' and i[0]+1 <= 4 and i[0]+2 <= 4 and board[i[0]+1, i[1]] == 'F' and board[i[0]+2,
                                                                                                        i[1]] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0]+1, i[1]] = 'O'
                    newboard[i[0]+2, i[1]] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard) # it will insert the newboard in the end of open list.
                        validmove(newboard) # generate childrens of the newboard
                        open_list.pop() # After generating the childrens remove the parent board.
                        closed_list.append(newboard)

            if board[i] == 'F' and i[0]-1 >= 0 and i[0]-2 >= 0 and board[i[0]-1, i[1]] == 'F' and board[i[0]-2,
                                                                                                        i[1]] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0]-1, i[1]] = 'O'
                    newboard[i[0]-2, i[1]] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard)
                        validmove(newboard)
                        open_list.pop()
                        closed_list.append(newboard)

            if board[i] == 'F' and i[0]+1 <= 4 and i[0]+2 <= 4 and i[1]-1 >= 0 and i[1]-2 >= 0 and board[i[0]+1,
                                                                                                         i[1]-1] == 'F' and board[i[0]+2, i[1]-2] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0]+1, i[1]-1] = 'O'
                    newboard[i[0]+2, i[1]-2] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard)
                        validmove(newboard)
                        open_list.pop()
                        closed_list.append(newboard)

            if board[i] == 'F' and i[1]+1 <= 4 and i[1]+2 <= 4 and board[i[0], i[1]+1] == 'F' and board[i[0],
                                                                                                        i[1]+2] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0], i[1]+1] = 'O'
                    newboard[i[0], i[1]+2] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard)
                        validmove(newboard)
                        open_list.pop()
                        closed_list.append(newboard)

            if board[i] == 'F' and i[1]-1 >= 0 and i[1]-2 >= 0 and board[i[0], i[1]-1] == 'F' and board[i[0],
                                                                                                        i[1]-2] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0], i[1]-1] = 'O'
                    newboard[i[0], i[1]-2] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard)
                        validmove(newboard)
                        open_list.pop()
                        closed_list.append(newboard)

            if board[i] == 'F' and i[1]+1 <= 4 and i[1]+2 <= 4 and i[0]-1 >= 0 and i[0]-2 >= 0 and board[i[0]-1,
                                                                                                         i[1]+1] == 'F' and board[i[0]-2, i[1]+2] == 'O':
                    newboard = copy.deepcopy(board)
                    newboard[i] = 'O'
                    newboard[i[0]-1, i[1]+1] = 'O'
                    newboard[i[0]-2, i[1]+2] = 'F'
                    if newboard not in open_list:
                        open_list.append(newboard)
                        validmove(newboard)
                        open_list.pop()
                        closed_list.append(newboard)

completeboard = fullboard(completeboard)

validmove(completeboard)
