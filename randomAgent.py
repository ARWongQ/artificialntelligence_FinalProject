import random

#This class holds the information of an agent that behaves randomly
class randomAgent:
    def __init__(self):
        self.name = "Random Agent"
        self.firstMove = None

    #Returns a random move between 0-8
    def getMove(self, world, possibleMoves, currentPlayer):
        if len(possibleMoves) == 1:
            return possibleMoves[0]
        else:
            i =random.randint(0,len(possibleMoves)-1)
            return possibleMoves[i]

    #Returs a wanting boards
    def getBoardMove(self, possibleBoards):
        if len(possibleBoards) == 1:
            return possibleBoards[0]
        else:
            i =random.randint(0,len(possibleBoards)-1)
            return possibleBoards[i]



