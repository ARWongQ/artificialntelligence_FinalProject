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
        rolloutNum = len(possibleMoves)
        wins = [0] * len(possibleMoves)
        randAgent = randomAgent()

        for i in xrange(rolloutNum):
            moveIdx = i%len(possibleMoves)
            firstMove = possibleMoves[moveIdx]
            self.firstMove = firstMove

            worldCopy = copy.deepcopy(world)

            winner = worldCopy.playThree(randAgent, randAgent)
            print('Finished one rollout\n')
            if winner == currentPlayer:
                wins[moveIdx] += 1

        chosenMove = wins.index(max(wins))

        return chosenMove


    #Returs a wanting boards
    def getBoardMove(self, possibleBoards):
        if len(possibleBoards) == 1:
            return possibleBoards[0]
        else:
            i =random.randint(0,len(possibleBoards)-1)
            return possibleBoards[i]

