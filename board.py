
from piece import Piece
class Board:

    def __init__(self, pieces , currentPosition):
        self.pieces = pieces
        self.size = 8
        self.currentPosition = currentPosition

    def addPiece(self,  p):
        self.pieces.append(p)
        
    def removePiece(self, p):
        self.pieces.remove(p)

    def selectPiece(self,coords):
        pos = Board.getPosFromCoords(coords)
        for piece in self.pieces:
            if piece.position == pos:
                return piece

        return None
    
    @staticmethod
    def getPosFromCoords(coords):
        return coords[0]//83, coords[1]//83 #division par 83 pour ramener position réelle sur l'écran à une coordonnée sur 8 cases (X * 8 / 664)
    

    def updateStringFromPieces(self):
        self.currentPosition = "00000000/00000000/00000000/00000000/00000000/00000000/00000000/00000000"
        for piece in self.pieces:
            index = piece.position[1]*9+piece.position[0]
            self.currentPosition = self.currentPosition[0:index] + piece.code + self.currentPosition[index+1:]
        copy = ""
        compteur = 0
        for i in range(len(self.currentPosition)):
            char = self.currentPosition[i]
            if char == "0":
                compteur += 1
                if i == len(self.currentPosition)-1:
                    copy += (str)(compteur)
            else:
                if compteur > 0:
                    copy += (str)(compteur)
                    compteur = 0

                copy += char

        self.currentPosition = copy

