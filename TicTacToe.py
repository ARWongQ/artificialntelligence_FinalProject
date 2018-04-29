from Node import Node

#Holds the information for simple tic tac toe
class TicTacToe:
    def __init__(self):
        self.grid = [[Node() for j in range(3)] for i in range(3)]
        self.hasWon = False
        self.wonBy = ''
        self.verbose = 0

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

    #Sets the winner for this tic tac toe board
    def setWinner(self, winner):
        #Don't do anything if this board has a winner
        if self.hasWon:
            return
        #print("There is a winner! " + winner)
        self.hasWon = True
        self.wonBy = winner

    #Check for all horizontal winners
    def horizontalWinner(self):
        #Don't do anything if this board already has a winner
        if self.hasWon:
            return

        #Check if there is a winner
        oCount = 0
        xCount = 0
        for i in xrange(3):
            for j in xrange(3):
                node = self.grid[i][j]
                #Break if any is empty
                if(node.isEmpty):
                    break

                elif(node.val == 'X'):
                    xCount += 1

                elif(node.val == 'O'):
                    oCount += 1

            #Check if anyCount is good enough to set winner
            if(xCount == 3):
                self.setWinner('X')

            elif(oCount == 3):
                self.setWinner('O')

            #None was good enough therefore check next line
            xCount = 0
            oCount = 0

    #Check for all vertical winners
    def verticalWinner(self):
        #Don't do anything if this board already has a winner
        if self.hasWon:
            return

        #Check if there is a winner
        oCount = 0
        xCount = 0
        for i in xrange(3):
            for j in xrange(3):
                node = self.grid[j][i]
                #Break if any is empty
                if(node.isEmpty):
                    break

                elif(node.val == 'X'):
                    xCount += 1

                elif(node.val == 'O'):
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
            node = self.grid[i][j]
            #Break if any is empty
            if(node.isEmpty):
                break

            elif(node.val == 'X'):
                xCount += 1

            elif(node.val == 'O'):
                oCount += 1

            #Update Index
            i +=1
            j +=1

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
            node = self.grid[i][j]
            #Break if any is empty
            if(node.isEmpty):
                break

            elif(node.val == 'X'):
                xCount += 1

            elif(node.val == 'O'):
                oCount += 1

            #Update Index
            i -=1
            j +=1

        #Check if anyCount is good enough to set winner
        if(xCount == 3):
            self.setWinner('X')


        elif(oCount == 3):
            self.setWinner('O')


    #Checks if the board has a winner, if so sets the winner
    def checkWinner(self):
        #Check Horizontal
        self.horizontalWinner()

        #Check Vertical
        self.verticalWinner()

        #Check diagonaly
        self.diagonalWinner()


    #retunrs the possiblemoves for this board
    def getPossibleMoves(self):
        possibleMoves = []
        for i in xrange(3):
            for j in xrange(3):
                node = self.grid[i][j]
                if(node.isEmpty):
                    possibleMoves.append(i*3 + j)
        return possibleMoves

    #Move
    def makeMove(self, world, currentPlayer, Agent1):
        if self.verbose:
            self.boardOptions()
            print("Current Player: " + currentPlayer)

        #Get all the possible actions for the boards
        possibleMoves = self.getPossibleMoves()

        #if no actions return none
        if(len(possibleMoves) == 0):
            return None


        if Agent1 != None:
            if Agent1.firstMove is None:
                move = Agent1.getMove(world, possibleMoves, currentPlayer)
            else:
                move = Agent1.firstMove
                Agent1.firstMove = None

        else:

            move = raw_input("Enter the number of your next move:")
            try:
                move = int(move)
            except ValueError:
                print("Please enter a valid move number between 0 and 8.")
                return self.makeMove(currentPlayer, Agent1)

            if move < 0 or move > 8:
                print("Move was invalid.")
                return self.makeMove(currentPlayer, Agent1)

        j = move % 3
        i = (move-j)/3
        if self.grid[i][j].isEmpty == False:
            print("Move was invalid.")
            #print("The move was " + str(move))
            #print("I= " + str(i) + " J=" + str(j) )
            return self.makeMove(world,currentPlayer, Agent1)
        else:
            self.grid[i][j].val = currentPlayer
            self.grid[i][j].isEmpty = False

            if self.verbose:
                print("Move " + str(move))
            return [i, j]



    #Print Board for Move
    def boardOptions(self):
        #Don't print board options if there are no moves
        if(len(self.getPossibleMoves()) == 0):
            return

        print("Available Spots: \n")

        string = ""
        for i in xrange(3):
            for j in xrange(3):
                node = self.grid[i][j]
                if(node.isEmpty == False):
                    string += node.val
                else:
                    string += str(i*3+j)
                if (j+1) % 3 != 0:
                    string += "|"
            string += "\n"
            if (i+1) % 3 != 0:
                string += "-|-|-\n"
        print(string)
