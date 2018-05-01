import random
import UltimateTTT
import copy

from randomAgent import randomAgent

#This class holds the information of an agent that uses rollout
class rolloutAgent:
    def __init__(self):
        self.name = "Rollout Agent"
        self.firstMove = None

    #Uses rollout to pick a next move
    def getMove(self, world, possibleMoves, currentPlayer):

        rolloutMultiplier = 500
        printInfo = 1000
        #print(possibleMoves)

        #500 rollouts per move
        rolloutNum = len(possibleMoves) * rolloutMultiplier

        wins = [0] * len(possibleMoves)

        #Do everything randomly after the first move
        randAgent = randomAgent()
        randAgent2 = randomAgent()

        for i in xrange(rolloutNum):
            #Keep track on which move to update
            moveIdx = i%len(possibleMoves)
            firstMove = possibleMoves[moveIdx]
            randAgent.firstMove = firstMove

            #Perform a random game on this UTTT board
            worldCopy = copy.deepcopy(world)
            worldCopy.setVerbose(0)

            winner = worldCopy.playThree(randAgent, randAgent2)
            # print('Finished one rollout\n')
            if winner == currentPlayer:
                wins[moveIdx] += 1

        chosenMove = wins.index(max(wins))
        # self.firstMove = None

        #     #After the game ended check who was the winner!
        #     winner = worldCopy.playThree(randAgent, randAgent2)
        #
        #     #print every 250 moves
        #     # if(i % printInfo == 0 and i != 0):
        #     #     print("Finished #" + str(i) +  " rollout\n")
        #
        #     #Utility function
        #     if(worldCopy.wonBy == currentPlayer):
        #         wins[moveIdx] += 20
        #
        #     for i in xrange(3):
        #         for j in xrange(3):
        #             TTTBoard =worldCopy.mainGrid[i][j]
        #             if(TTTBoard.wonBy == currentPlayer):
        #                 wins[moveIdx] += 1
        #             elif(TTTBoard.wonBy == 'O'):
        #                 wins[moveIdx] -= 0.5
        #
        # chosenMove = wins.index(max(wins))
        #self.firstMove = None

        return possibleMoves[chosenMove]


    #Returns a wanting boards
    def getBoardMove(self, possibleBoards):
        #pick a board
        if len(possibleBoards) == 1:
            return possibleBoards[0]
        else:
            i =random.randint(0,len(possibleBoards)-1)
            return possibleBoards[i]

