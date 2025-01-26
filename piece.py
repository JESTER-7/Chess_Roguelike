from abc import ABC, abstractmethod

class Piece():

    def __init__(self, code, image, color, position):
        self.code = code
        self.image = image
        self.color = color
        self.position = position


    def isMoveLegal(move):
        pass


    def getAllLegalMoves():
        pass

