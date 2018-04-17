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
        self.boardOptions()
        move = raw_input("Enter the number of your next move:")
        move = int(move)
        j = move % 3
        i = (move-j)/3
        if self.grid[i][j].isEmpty == False:
            print("Move was invalid.")
            return self.makeMove()
        else:
            self.grid[i][j].val = 'X'
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
