from TicTacToe import TicTacToe

#Holds the entire information
class UltimateTTT:
    def __init__(self):
        self.mainGrid = [[TicTacToe() for j in range(3)] for i in range(3)]
        self.currentBoard = [1, 1]
        self.hasWon = False
        self.wonBy = ' '
        self.currentPlayer = 'X'

    #Displays winners of the entire UTTT
    def displayWinningBoards(self):
        print("The board's result!")

        string = ""
        for i in xrange(3):
            for j in xrange(3):

                boardTTT = self.mainGrid[i][j]

                if(boardTTT.hasWon):
                    string += boardTTT.wonBy
                else:
                    string += "N"

                string += " |"


                if(((i*3 + j)+1) % 3 == 0 and j != 0):
                    string += "\n"

        print string



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

        self.displayWinningBoards()

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



    #Check for tie
    #Tie happens when all tic tac toe boards are taken and there is still no winner
    def checkTie(self):
        #Loop through all the tic tac toe boards and check if they all have a winner

        for i in xrange(3):
            for j in xrange(3):
                #Check if not taken
                if(self.mainGrid[i][j].hasWon == False):
                    return

        #They all have been taken set as won (Terminal State)
        if(self.hasWon):
            return

        print("There is TIE! ")
        self.hasWon = True
        self.displayWinningBoards()


    # Tie happens when all tic tac toe boards are taken and there is still no winner
    def checkNoMoves(self):
        # Loop through all the tic tac toe boards and check if they all have a winner

        for i in xrange(3):
            for j in xrange(3):
                # Check if not taken
                if (len(self.mainGrid[i][j].getPossibleMoves()) > 0):
                    return

        # They all have been taken set as won (Terminal State)
        if (self.hasWon):
            return

        print("There is TIE! ")
        self.hasWon = True


    #checks if the Ultimate tic tac toe board has a winner
    def checkWinner(self):
        #Check horizontal
        self.horizontalWinner()
        #Check vertically
        self.verticalWinner()
        #check diagonally
        self.diagonalWinner()
        #check for tie
        self.checkTie()
        #check for no more available moves
        self.checkNoMoves()

    #Prints available boards
    def displayAvailableBoards(self):
        print("Pick any avialable board")

        string = ""
        for i in xrange(3):
            for j in xrange(3):
                possibleMoves = self.mainGrid[i][j].getPossibleMoves()

                if(len(possibleMoves) == 0):
                    string += "N"

                else:
                    string += str(i*3 + j)

                string += " |"


                if(((i*3 + j)+1) % 3 == 0 and j != 0):
                    string += "\n"

        print string

    #Lets the agent/user pick a board
    def pickBoard(self,Agent, possibleBoards):
        if(Agent == None):
            #Print available shit to the user
            self.displayAvailableBoards()
            move = raw_input("Enter the number of your Board move:")
            try:
                move = int(move)
            except ValueError:
                print("Please enter a valid move number between 0 and 8.")
                return self.pickBoard(Agent, possibleBoards)

            if move < 0 or move > 8:
                print("Move was invalid.")
                return self.pickBoard(Agent, possibleBoards)

            return move

        else:
            return Agent.getBoardMove(possibleBoards)



    #Move
    def move(self, Agent1):
        currentBoard = self.currentBoard

        newBoard = self.mainGrid[currentBoard[0]][currentBoard[1]].makeMove(self,self.currentPlayer, Agent1)
        while(newBoard == None):
            possibleBoards = []
            for i in xrange(3):
                for j in xrange(3):
                    possibleMoves = self.mainGrid[i][j].getPossibleMoves()
                    #Check if no moves available
                    if(len(possibleMoves) != 0):
                        possibleBoards.append(i*3 + j)

            #Gets the available boards
            boardMove = self.pickBoard(Agent1, possibleBoards)



            j = boardMove % 3
            i = (boardMove-j)/3

            currentBoard = [i,j]
            TTT = self.mainGrid[currentBoard[0]][currentBoard[1]]
            if(TTT != None):
                print("New Selected Board is " + str(boardMove) + "\n")

            newBoard = self.mainGrid[currentBoard[0]][currentBoard[1]].makeMove(self,self.currentPlayer, Agent1)




        else:
            self.currentBoard = newBoard
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
    def playThree(self, rAgent1, rAgent2):
        for i in xrange(81):
            if(i%2 == 0):
                self.move(rAgent1)
            else:
                self.move(rAgent2)

            self.checkWinner()
            if self.hasWon:
                # self.displayBoard()
                return self.wonBy

        self.displayBoard()
        print('No Winner!')
        return None

