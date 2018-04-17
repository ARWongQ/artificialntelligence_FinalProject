from Node import Node

#Holds the information for simple tic tac toe
class TicTacToe:
    def __init__(self):
        self.grid = [[Node() for j in range(3)] for i in range(3)]

    #Gets the line as a string for display
    def getLineString(self, lineNumb):
        str = ""
        for i in xrange(3):
            node = self.grid[lineNumb][i]
            if(node.isEmpty == False):
                str += node.val
            else:
                str += " "

        return str

    #Win
    def win(self):
        pass

    #Move
    def makeMove(self):
        pass
