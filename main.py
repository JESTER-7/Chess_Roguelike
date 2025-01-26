import pygame 
from piece import Piece
from move import Move
from board import Board

windowsSize = 664
squareSide = windowsSize/8
pygame.init()
screen = pygame.display.set_mode((windowsSize, windowsSize))
running = True
green = (131, 183, 81)  
white = (255 ,255 ,255) 
yellow = (250, 189, 22)
currentColor = 1
startingPosition = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
charWithImage = {"r":"images/Brook.png", "n":"images/Bknight.png", "b":"images/Bbishop.png","q":"images/Bqueen.png", "k":"images/Bking.png", "p":"images/Bpawn.png",
                     "R":"images/Wrook.png", "N":"images/Wknight.png", "B":"images/Wbishop.png","Q":"images/Wqueen.png", "K":"images/Wking.png", "P":"images/Wpawn.png"}

possibleMoves = []

def drawSquareFromCoords(coords, color=""):
     rect = pygame.Rect(coords[0], coords[1], squareSide, squareSide )  # Create a rectangle (x, y, width, height)

     if color == yellow:
           pygame.draw.rect(screen, yellow, rect)  # Draw the rectangle on the screen
     else:
           
          if (coords[0]+coords[1])%2 == 0:
                         pygame.draw.rect(screen, white, rect)  # Draw the rectangle on the screen 
          else:
                         pygame.draw.rect(screen, green, rect)  # Draw the rectangle on the screen

def drawSquares():

     for colonne in range(8):
          for ligne in range(8):
               
               drawSquareFromCoords((ligne*squareSide,colonne*squareSide))

board = Board([], startingPosition)

def initiatePieces(currentPosition):
     compteur = 0
     compteurInter = 0
     number = 0
     while compteur < len(board.currentPosition):
          piece = board.currentPosition[compteur]

          if piece.isnumeric():
                    number += (int)(piece)-1

          elif piece in "rnbqkpRNBQKP":
               x = (compteur-compteurInter+number)%8
               y = (compteur-compteurInter+number)//8
               pieceObject = Piece(piece, charWithImage[piece], ord(piece)//91, (x,y))
               board.addPiece(pieceObject)

          else:
               compteurInter += 1
                    
          compteur += 1


def drawPieces():
     for piece in board.pieces:
          screen.blit(pygame.image.load(piece.image).convert_alpha(), (piece.position[0]*squareSide,piece.position[1]*squareSide))
               

drawSquares()
initiatePieces(board.currentPosition)
drawPieces()



movedPiece = None  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    mouseButtons = pygame.mouse.get_pressed()
    if mouseButtons[0] and movedPiece == None:
         
         mousePos = pygame.mouse.get_pos()
         selectedPiece = board.selectPiece(mousePos)

         if selectedPiece != None and selectedPiece.color != currentColor:
               movedPiece = Piece(selectedPiece.code, selectedPiece.image, selectedPiece.color, selectedPiece.position)
               
    
    if mouseButtons[0] and movedPiece != None:
         mousePos = pygame.mouse.get_pos()
         drawSquares()
         drawPieces()
         drawSquareFromCoords((selectedPiece.position[0]*squareSide, selectedPiece.position[1]*squareSide), yellow)
         screen.blit(pygame.image.load(movedPiece.image).convert_alpha(), (mousePos[0]-squareSide/2,mousePos[1]-squareSide/2))
         
    
    if (not mouseButtons[0]) and movedPiece != None:
     
         movedPiece.position = Board.getPosFromCoords(mousePos)
         movedPieceCoords = mousePos
         if movedPieceCoords[0] >= 0 and movedPieceCoords[0] <= windowsSize-1 and movedPieceCoords[1] >= 0 and movedPieceCoords[1] <= windowsSize-1:
          move = Move("", selectedPiece, movedPieceCoords, board)
          if move.isMoveLegal():
                
               eatenPiece = board.selectPiece((movedPieceCoords[0], movedPieceCoords[1]))
               if eatenPiece != None:
                         if eatenPiece.color != movedPiece.color:
                              board.removePiece(eatenPiece)
                         else:
                              movedPiece = None
               
               if movedPiece != None:
                         currentColor = (currentColor+1)%2
                         board.addPiece(movedPiece)
                         board.removePiece(selectedPiece)
                         board.updateStringFromPieces()
         else:
               movedPiece = None
         drawSquares()
         drawPieces()
         
         
         movedPiece = None

  
    pygame.display.update()

pygame.quit()   