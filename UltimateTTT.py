from TicTacToe import TicTacToe

#Holds the entire information
class UltimateTTT:
    def __init__(self):
        self.mainGrid = [[TicTacToe() for j in range(3)] for i in range(3)]
        self.currentBoard = [1, 1]

    #Displays the current board
    def displayBoard(self):
        str = ""
        for k in xrange(3):
            for i in xrange(3):
                for j in xrange(3):
                    str += self.mainGrid[k][j].getLineString(i)
                    if (j+1) % 3 != 0:
                        str += "|"

                str += "\n"
            if (k+1) % 3 != 0:
                str += "-----------"
            str += "\n"
        print(str)

    #Win
    def win(self):
        pass

    #Move
    def move(self):
        currentBoard = self.currentBoard
        self.currentBoard = self.mainGrid[currentBoard[0]][currentBoard[1]].makeMove()

    #Play
    def play(self):
        for i in xrange(10):
            self.displayBoard()
            self.move()
