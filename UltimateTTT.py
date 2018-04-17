from TicTacToe import TicTacToe

#Holds the entire information
class UltimateTTT:
    def __init__(self):
        self.mainGrid = [[TicTacToe() for j in range(3)] for i in range(3)]

    #Displays the current board
    def displayBoard(self):
        str = ""
        for k in xrange(3):
            for i in xrange(3):
                for j in xrange(3):
                    str += self.mainGrid[k][j].getLineString(i)
                    str += "|"

                str += "\n"
            str += "-------------"
            str += "\n"
        print(str)

    #Win
    def win(self):
        pass

    #Move
    def move(self):
        pass
