from TicTacToe import TicTacToe

#Holds the entire information
class UltimateTTT:
    def __init__(self):
        self.mainGrid = [[TicTacToe() for j in range(3)] for i in range(3)]
        self.currentBoard = [1, 1]
        self.hasWon = False
        self.wonBy = ' '
        self.currentPlayer = 'X'

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


    #Sets the winner of the game!
    def setWinner(self, winner):
        if(self.hasWon):
            return
        print("The Ultimate Tic Tac Toe Winner is " + winner)
        self.hasWon = True
        self.wonBy = winner
        #Do something to stop the program!

    #Check for a winner in the horizontal lines
    def horizontalWinner(self):
        #Check if there is a winner
        oCount = 0
        xCount = 0
        for i in xrange(3):
            for j in xrange(3):
                TTT = self.mainGrid[i][j]

                #Break if the board does not have a winner yet
                if(TTT.hasWon == False):
                    break

                elif(TTT.wonBy == 'X'):
                    xCount += 1

                elif(TTT.wonBy == 'O'):
                    oCount += 1

            #Check if anyCount is good enough to set winner
            if(xCount == 3):
                self.setWinner('X')

            elif(oCount == 3):
                self.setWinner('O')

            #None was good enough therefore check next line
            xCount = 0
            oCount = 0

    #Check for a winner in the vertical lines
    def verticalWinner(self):
        #Check if there is a winner
        oCount = 0
        xCount = 0
        for i in xrange(3):
            for j in xrange(3):
                TTT = self.mainGrid[j][i]

                #Break if the board does not have a winner yet
                if(TTT.hasWon == False):
                    break

                elif(TTT.wonBy == 'X'):
                    xCount += 1

                elif(TTT.wonBy == 'O'):
                    oCount += 1

            #Check if anyCount is good enough to set winner
            if(xCount == 3):
                self.setWinner('X')

            elif(oCount == 3):
                self.setWinner('O')

            #None was good enough therefore check next line
            xCount = 0
            oCount = 0

    #Check for all diagonal winners
    def diagonalWinner(self):
        #Check for \ diagonal
        i = 0
        j = 0

        oCount = 0
        xCount = 0
        for x in xrange(3):
            TTT = self.mainGrid[i][j]
            #Break if the board does not have a winner yet
            if(TTT.hasWon == False):
                break

            elif(TTT.wonBy == 'X'):
                xCount += 1

            elif(TTT.wonBy == 'O'):
                oCount += 1

            #Update index
            i += 1
            j += 1

        #Check if anyCount is good enough to set winner
        if(xCount == 3):
            self.setWinner('X')
            return

        elif(oCount == 3):
            self.setWinner('O')
            return

        #None was good enough therefore check other diagonal
        #Check for / diagonal
        oCount = 0
        xCount = 0

        i = 2
        j = 0
        for x in xrange(3):
            TTT = self.mainGrid[i][j]
            #Break if the board does not have a winner yet
            if(TTT.hasWon == False):
                break

            elif(TTT.wonBy == 'X'):
                xCount += 1

            elif(TTT.wonBy == 'O'):
                oCount += 1

            #Update index
            i -= 1
            j += 1

        #Check if anyCount is good enough to set winner
        if(xCount == 3):
            self.setWinner('X')

        elif(oCount == 3):
            self.setWinner('O')





    #checks if the Ultimate tic tac toe board has a winner
    def checkWinner(self):
        #Check horizontal
        self.horizontalWinner()
        #Check vertically
        self.verticalWinner()
        #check diagonally
        self.diagonalWinner()


    #checks the number of moves left in the Ultimate tic tac toe board
    def moveNum(self):
        pass

    #Move
    def move(self, Agent1):
        currentBoard = self.currentBoard
        self.currentBoard = self.mainGrid[currentBoard[0]][currentBoard[1]].makeMove(self.currentPlayer, Agent1)
        self.mainGrid[currentBoard[0]][currentBoard[1]].checkWinner()
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

    #Plays Player v Player
    def play(self):
        for i in xrange(82):
            self.displayBoard()
            self.move(None)
            self.checkWinner()
            if self.hasWon:
                self.displayBoard()
                return

    #
    def moveAgent(self):
        pass

    #Plays Player v Cpu
    def playTwo(self, Agent1):
        for i in xrange(82):
            self.displayBoard()

            if(i%2 == 0):
                self.move(None)
            else:
                self.move(Agent1)


            self.checkWinner()
            if self.hasWon:
                self.displayBoard()
                return



    #Plats Cpu v Cpu
    def playThree(self, Agent1, Agent2, firstMove):
        for i in xrange(81):
            if(i%2 == 0):
                self.move(Agent1)
            else:
                self.move(Agent2)

            self.checkWinner()
            if self.hasWon:
                # self.displayBoard()
                return self.wonBy

        self.displayBoard()
        print('No Winner!')
        return None

