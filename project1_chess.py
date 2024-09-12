'''
This project  will model a chess board and chess piece movements using Python. 

After modeling the chess board and chess pieces, the code will take simple user input
that will attempt to place chess pieces on the chess board. The code will remember
which pieces have been placed so far and figure out whether the user’s current piece can be
placed at the indicated square. If the indicated square is empty, the code will place the
new piece on that square and remember that the square is occupied for future user input. At this
point, the  code will also calculate and print how many squares the new piece can move
based on its location, its piece type, and the vacancy of other squares on the chess board.

User input will be received in this format:
"<Piece Color> <Piece Name> <Square>"

Possible Piece Colors: White, Black
Possible Piece Names: Pawn, Knight, Bishop, Rook, Queen, King
Possible Squares: E4, G5, A7, etc 
(read how Chess square names work: https://en.wikipedia.org/wiki/Algebraic_notation_(chess) )

Example of User's interaction with the chess program:

What piece would you like to place, and where? --> White Bishop F2
White Bishop at F2 can move to 9 unique squares.
What piece would you like to place, and where? --> White Pawn A2
White Bishop at A2 can move to 2 unique squares.
What piece would you like to place, and where? --> Black Rook A1
Black Rook at A1 can move to 8 unique squares.
What piece would you like to place, and where? --> STOP
Thank you for playing!

Some more notes:
-You will always start off with an empty board every time the user starts your program.
-As you can see above, you need to factor in the cases where white pieces and black pieces
 can capture each other. Pieces with the same color can't capture each other. This will impact
 how many moves a given piece on the board can make. On an empty board, the Black Rook at A1
 should be able to move to 14 unique squares. However, the White Pawn on A2 is in its way,
 which limits the Rook's movement. However, the Rook can still capture the pawn, which should
 count as a move. If the Pawn was Black instead of White, the Rook would not be able to capture
 it, and would only have 7 possible moves.


'''


board = [["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
         ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
         ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
         ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
         ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
         ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
         ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"],
         ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]]

'''
Create dictionary with square as the key and the color as the value to check if a square is filled
'''

chessBoard = {}

# Bishop
def Bishop(rowIndex, colIndex, colorPiece):
    squaresMovable = 0

    tempRow = rowIndex + 1
    tempCol = colIndex + 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow += 1
        tempCol += 1

    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex + 1
    tempCol = colIndex - 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow += 1
        tempCol -= 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex - 1
    tempCol = colIndex + 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow -= 1
        tempCol += 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex - 1
    tempCol = colIndex - 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow -= 1
        tempCol -= 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    return squaresMovable

# Rook
def Rook(rowIndex, colIndex, colorPiece):
    squaresMovable = 0

    tempRow = rowIndex + 1
    tempCol = colIndex

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow += 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex - 1
    tempCol = colIndex

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempRow -= 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex
    tempCol = colIndex + 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempCol += 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    tempRow = rowIndex
    tempCol = colIndex - 1

    while tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and (tempRow, tempCol) not in chessBoard.keys():
        squaresMovable += 1

        tempCol -= 1
    
    if (tempRow, tempCol) in chessBoard.keys() and chessBoard[(tempRow, tempCol)] != colorPiece:
        squaresMovable += 1
    
    return squaresMovable

# Queen
def Queen(rowIndex, colIndex, colorPiece):
    return Rook(rowIndex, colIndex, colorPiece) + Bishop(rowIndex, colIndex, colorPiece)

# King
def King(rowIndex, colIndex, colorPiece):
    squaresMovable = 0

    tempRow = rowIndex + 1
    tempCol = colIndex
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex - 1
    tempCol = colIndex
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex
    tempCol = colIndex + 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex
    tempCol = colIndex - 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex + 1
    tempCol = colIndex + 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex - 1
    tempCol = colIndex + 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex + 1
    tempCol = colIndex - 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1

    tempRow = rowIndex - 1
    tempCol = colIndex - 1
        
    if tempRow <= 7 and tempCol <= 7 and tempRow >= 0 and tempCol >= 0 and ((tempRow, tempCol) not in chessBoard.keys() or (chessBoard[(tempRow, tempCol)] != colorPiece)):
        squaresMovable += 1
    
    return squaresMovable
    
# Pawn
def Pawn(rowIndex, colIndex, colorPiece):
    squaresMovable = 0

    if colorPiece == "White" and colIndex == 1:
        squaresMovable = 2
    elif colorPiece == "Black" and colIndex == 6:
        squaresMovable = 2

    if colorPiece == "White":
        tempRow = rowIndex + 1
        tempCol = colIndex + 1

        if (tempRow, tempCol) in chessBoard.keys():
            if chessBoard[(tempRow, tempCol)] != colorPiece:
                squaresMovable += 1

        tempRow = rowIndex - 1
        tempCol = colIndex + 1

        if (tempRow, tempCol) in chessBoard.keys():
            if chessBoard[(tempRow, tempCol)] != colorPiece:
                squaresMovable += 1

    elif colorPiece == "Black":
        tempRow = rowIndex - 1
        tempCol = colIndex - 1

        if (tempRow, tempCol) in chessBoard.keys():
            if chessBoard[(tempRow, tempCol)] != colorPiece:
                squaresMovable += 1

        tempRow = rowIndex + 1
        tempCol = colIndex - 1

        if (tempRow, tempCol) in chessBoard.keys():
            if chessBoard[(tempRow, tempCol)] != colorPiece:
                squaresMovable += 1

    return squaresMovable
        
# Knight
def Knight(rowIndex, colIndex, colorPiece):
    squaresMovable = 0

    tempCol = colIndex + 1
    tempRow = rowIndex - 2

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex + 1
    tempRow = rowIndex + 2

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex + 2
    tempRow = rowIndex - 1

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex + 2
    tempRow = rowIndex + 1

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex - 1
    tempRow = rowIndex - 2

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex - 1
    tempRow = rowIndex + 2

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex - 2
    tempRow = rowIndex - 1

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    tempCol = colIndex - 2
    tempRow = rowIndex + 1

    colAndRowInRange = tempCol <= 7 and tempRow <= 7 and tempRow >= 0 and tempCol >= 0

    if colAndRowInRange and ((tempRow, tempCol) not in chessBoard.keys() or chessBoard[(tempRow, tempCol)] != colorPiece):
        squaresMovable += 1

    return squaresMovable


userInput = input("What piece would you like to put and where(Enter 'STOP' if you would like to exit the program)===> ") + " "

while userInput != "STOP ":

    color = userInput[0 : 5]
    piece = userInput[6 : len(userInput) - 4]
    square = userInput[-3 : -1]

    # Find Index of square
    rowIndex = -1
    colIndex = -1

    row = 0

    while rowIndex < 0 and row <= 7:
        if board[row].count(square) > 0:
            rowIndex = row
            colIndex = board[row].index(square)
        
        row += 1

    chessBoard[(rowIndex, colIndex)] = color
    
    if piece == "Bishop":
        print(color, piece, "on", square, "can move to", Bishop(rowIndex, colIndex, color), "unique squares.")

    elif piece == "Rook":
        print(color, piece, "on", square, "can move to", Rook(rowIndex, colIndex, color), "unique squares.")

    elif piece == "Queen":
        print(color, piece, "on", square, "can move to", Queen(rowIndex, colIndex, color), "unique squares.")

    elif piece == "King":
        print(color, piece, "on", square, "can move to", King(rowIndex, colIndex, color), "unique squares.")

    elif piece == "Pawn":
        print(color, piece, "on", square, "can move to", Pawn(rowIndex, colIndex, color), "unique squares.")

    elif piece == "Knight":
        print(color, piece, "on", square, "can move to", Knight(rowIndex, colIndex, color), "unique squares.")

    userInput = input("What piece would you like to put and where(Enter 'STOP' if you would like to exit the program)===> ") + " "

print("Thank you for playing!")
