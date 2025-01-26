from piece import Piece
from board import Board

class Move:

    def __init__(self, id, piece, newSquareCoords,board):
        self.id = id
        self.piece = piece
        self.board = board
        self.newSquareCoords = newSquareCoords

    def isMoveLegal(self):
        pos = Board.getPosFromCoords(self.newSquareCoords)
        newSquareDistance = (abs(self.piece.position[0] - pos[0]), abs(self.piece.position[1]-pos[1]))

        if self.piece.code.lower() == "n":
            return (newSquareDistance[0] == 2 and newSquareDistance[1] == 1) or (newSquareDistance[0] == 1 and newSquareDistance[1] == 2)
            
        elif self.piece.code == "p":

            return  (self.piece.position[1]-pos[1]==-1 and newSquareDistance[0] == 0 and self.board.selectPiece(self.newSquareCoords) == None) or (self.piece.position[1]==1 and self.board.selectPiece(self.newSquareCoords) == None and newSquareDistance[0] == 0 and self.piece.position[1]-pos[1]==-2 ) or (self.piece.position[1]-pos[1]==-1 and self.board.selectPiece(self.newSquareCoords) != None and abs(self.piece.position[0]-pos[0])==1)
        
        elif self.piece.code == "P":
            return self.piece.position[1]-pos[1]==1 and newSquareDistance[0] == 0 and self.board.selectPiece(self.newSquareCoords) == None or (self.piece.position[1]==6 and self.board.selectPiece(self.newSquareCoords) == None and newSquareDistance[0] == 0 and self.piece.position[1]-pos[1]==2) or (self.piece.position[1]-pos[1]==1 and self.board.selectPiece(self.newSquareCoords) != None and abs(self.piece.position[0]-pos[0])==1)
        
        elif self.piece.code.lower() == "b": 
            return newSquareDistance[0] == newSquareDistance[1]
        
        elif self.piece.code.lower() == "q":
            return (newSquareDistance[0] == newSquareDistance[1]) or ((newSquareDistance[0] == 0 and newSquareDistance[1] != 0)or (newSquareDistance[1] == 0 and newSquareDistance[0]!=0))
        
        elif self.piece.code.lower() == "k":
            return (newSquareDistance[0] == newSquareDistance[1] == 1) or ((newSquareDistance[0] == 0 and newSquareDistance[1] == 1)or (newSquareDistance[1] == 0 and newSquareDistance[0]==1))
        
        elif self.piece.code.lower() == "r":
           return  (newSquareDistance[0] == 0 and newSquareDistance[1] != 0) or (newSquareDistance[1] == 0 and newSquareDistance[0]!=0)
        return False

        