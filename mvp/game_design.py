#!/usr/bin/python

import random
import sys

def drawBoard(board):
    NLINE = "     1   2   3   4   5   6   7   8"
    HLINE = "   +---+---+---+---+---+---+---+---+"
    VLINE = "   |   |   |   |   |   |   |   |   |"
    print NLINE
    print HLINE
    for y in range(8):
        print VLINE
        print y+1,'', 
        for x in range(8):
            print "| %s"%(board[x][y]),
        print "|" 
        print VLINE
        print HLINE

def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = " "
    board[3][3] = "X"
    board[3][4] = "O"
    board[4][3] = "O"
    board[4][4] = "X"

def getNewBoard():
    board = []
    for i in range(8):
        board.append([" "]*8)
    return board

def getBoardCopy(board):
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def isOnBoard(x, y):
    return (x>=0 and x<=7 and y>=0 and y<=7)

def isOnCorner(x, y):
    return (x==0 or x==7) and (y==0 or y==7)

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    tile = ''
    while not (tile=='X' or tile=='O'):
        print "Do you want to be X or O?"
        tile = raw_input().upper()
        if tile=='X':
            return ['X','O']
        else:
            return ['O','X']

def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'Computer'
    else:
        return 'Player'


def showPoints(playerTile, computerTile):
    scores = getScoreOfBoard(mainBoard)
    print "You have %s points, The computer has %s points"%(scores[playerTile], scores[computerTile])

def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def isValidMove(board, tile, xstart, ystart):
    if (board[xstart][ystart] != ' ') or (not isOnBoard(xstart, ystart)):
        return False
    board[xstart][ystart] = tile
    otherTile = 'O' 
    if tile=='O': 
        otherTile = 'X'

    tilesToFlip = []
    direction = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for xd, yd in direction:
        x, y = xstart, ystart
        x += xd
        y += yd
        if isOnBoard(x, y) and board[x][y]==otherTile:
           x += xd
           y += yd
           if not isOnBoard(x, y):
               continue
           while board[x][y] == otherTile:
               x += xd
               y += yd
               if not isOnBoard(x, y):
                  break
           if not isOnBoard(x, y):
               continue
           if board[x][y] == tile:
               while True:
                   x -= xd
                   y -= yd
                   if x==xstart and y==ystart:
                       break
                   tilesToFlip.append([x, y])
    board[xstart][ystart] = ' ' # back to before
    if len(tilesToFlip)==0:
        return False

    return tilesToFlip

def makeMove(board, tile, xstart, ystart):
    #Place the tile on the board at xstart and ystart, and flip any of the opponent's pieces
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getPlayerMove(board, playerTile):
    DIGIT = '1 2 3 4 5 6 7 8'.split()
    while True:
        print "Enter your move, or type quit to end the game."
        move = raw_input().lower()
        if move == 'quit':
            return move

        if len(move)==2 and (move[0] in DIGIT) and (move[1] in DIGIT):
            x = int(move[0])-1
            y = int(move[1])-1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print "That is not a valid move. Type the x digit (1-8), then the y digit (1-8)."
            print "For example, 81 whill be the top-right corner."

    return [x,y]

def getComputerMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    # always go for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # go throught all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def showPoints(playerTile, computerTile):
    scores = getScoreOfBoard(mainBoard)
    print "You have %s points, The computer has %s points"%(scores[playerTile], scores[computerTile])


print "Welcome to Reversi ..."
print
print "######## instruction ########"
print "Your input is valid if changing opponent's tile"
print "#############################"
print

while True:
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    turn = whoGoesFirst()
    print "The %s will go first."%(turn)

    while True: # onece player
        if turn == 'Player':
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print "Thanks for playing!"
                sys.exit()
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])

            if getValidMoves(mainBoard, computerTile)==[]:
                break;
            else:
                turn = 'Computer'

        else: # Computer
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            raw_input('Press Enter to see the computer\'s move.')
            move = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, move[0], move[1])
            if getValidMoves(mainBoard, playerTile)==[]:
                break
            else:
                turn = 'Player'

    # Display the final score.
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print ('X scored %s points. O scored %s points.'%(scores['X'], scores['O']))
    points = scores[playerTile] - scores[computerTile]
    if points>0:
        print "You beat the computer by %s points! Congratulations!"%(points)
    elif points<0:
        print "You lost. The computer beat you by %s points."%(0-points)
    else:
        print "The game was a tie."

    play = False;
    while True:
        print "Do you want to play again ?  (y/n)"
        if raw_input().lower()=='y':
            play = True
            break
        elif raw_input().lower()=='n':
            play == False
            break
    if play==False:
        break

