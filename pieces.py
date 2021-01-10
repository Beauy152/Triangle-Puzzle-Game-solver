RED = 'red'
GRN = 'green'
BLU = 'blue'
WHT = 'white'
BLK = 'black'
YLW = 'yellow'
NA = 'none'
UP = 'up'
DOWN = 'down'


class Piece:
    def __init__(self,c1,c2,c3):
        self.orientation = UP
        self.l = c1
        self.m = c2
        self.r = c3

    def rotate(self,n=1):
        """rotates piece orientation n times
        rotating a piece once will flip its orientation,
        twice will keep orientation, while changing permuation"""
        for _ in range(n):
            if self.orientation == UP: 
                self.m,self.r = self.r,self.m
                self.orientation = DOWN
            else: 
                self.l,self.m = self.m,self.l
                self.orientation = UP

    def rotate_2(self):
        self.rotate(n=2)

    def getCols(self):
        return [self.l,self.m,self.r]

    def __repr__(self):
        return "{0},{1},{2}".format(self.l,self.m,self.r)

NULL = Piece(NA,NA,NA)

def getPieces():
    return [
        Piece(YLW,GRN,WHT),#
        Piece(BLK,BLU,WHT),#
        Piece(YLW,GRN,WHT),#
        Piece(WHT,BLU,WHT),#
        Piece(GRN,YLW,BLU),#
        Piece(YLW,BLK,GRN),#
        Piece(BLU,BLK,YLW),#
        Piece(GRN,BLK,RED),#
        Piece(GRN,BLK,BLK),#
        Piece(YLW,WHT,RED),#
        Piece(BLK,GRN,RED),#
        Piece(YLW,GRN,RED),#
        Piece(BLK,RED,GRN),#
        Piece(WHT,BLU,BLU),#
        Piece(WHT,BLK,BLU),#
        Piece(GRN,RED,WHT),#
        #all pieces have been verified
    ]

def getBoard():
    return [
        [Piece(GRN,GRN,GRN),None,Piece(YLW,YLW,YLW)],
        [Piece(GRN,GRN,GRN),None,None,None,Piece(WHT,WHT,WHT)],
        [Piece(WHT,WHT,WHT),None,None,None,None,None,Piece(RED,RED,RED)],
        [Piece(GRN,GRN,GRN),None,None,None,None,None,None,None,Piece(WHT,WHT,WHT)],
        [NULL,Piece(BLK,BLK,BLK),NULL,Piece(GRN,GRN,GRN),NULL,Piece(RED,RED,RED),NULL,Piece(BLU,BLU,BLU),NULL]
    ]