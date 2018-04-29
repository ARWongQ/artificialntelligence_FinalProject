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
        printInfo = 250
        rolloutMultiplier = 500
        #print(possibleMoves)

        #500 rollouts per move
        rolloutNum = len(possibleMoves) * rolloutMultiplier

        wins = [0] * len(possibleMoves)

        #Do everything randomly after the first move
        randAgent = randomAgent()

        for i in xrange(rolloutNum):
            #Keep track on which move to update
            moveIdx = i%len(possibleMoves)
            firstMove = possibleMoves[moveIdx]
            self.firstMove = firstMove

            #Perform a random game on this UTTT board
            worldCopy = copy.deepcopy(world)
            worldCopy.setVerbose(0)

            #After the game ended check who was the winner!
            winner = worldCopy.playThree(randAgent, randAgent)

            #print every 250 moves
            if(i % printInfo == 0 and i != 0):
                print("Finished #" + str(i) +  " rollout\n")


            if winner == currentPlayer:
                wins[moveIdx] += 1

        chosenMove = wins.index(max(wins))
        self.firstMove = None

        return possibleMoves[chosenMove]


    #Returns a wanting boards
    def getBoardMove(self, possibleBoards):
        #pick a board
        if len(possibleBoards) == 1:
            return possibleBoards[0]
        else:
            i =random.randint(0,len(possibleBoards)-1)
            return possibleBoards[i]

