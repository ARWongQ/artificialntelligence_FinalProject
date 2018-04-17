from Node import Node

#Holds the information for simple tic tac toe
class TicTacToe:
    def __init__(self):
        self.grid = [[Node() for j in range(3)] for i in range(3)]
        self.hasWon = False
        self.wonBy = ''

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
        print("There is a winner! " + winner)
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


    #Move
    def makeMove(self, currentPlayer, Agent1):
        self.boardOptions()
        print("Current Player: " + currentPlayer)
        if Agent1 != None:
            move = Agent1.getMove()

        else:
            move = raw_input("Enter the number of your next move:")
            move = int(move)

        j = move % 3
        i = (move-j)/3
        if self.grid[i][j].isEmpty == False:
            print("Move was invalid.")
            return self.makeMove(currentPlayer, Agent1)
        else:
            self.grid[i][j].val = currentPlayer
            self.grid[i][j].isEmpty = False
            return [i, j]



    #Print Board for Move
    def boardOptions(self):
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
