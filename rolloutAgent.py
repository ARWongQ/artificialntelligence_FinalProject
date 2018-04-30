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
        rolloutNum = len(possibleMoves)*50
        wins = [0] * len(possibleMoves)
        randAgent = randomAgent()
        randAgent2 = randomAgent()

        for i in xrange(rolloutNum):
            moveIdx = i%len(possibleMoves)
            firstMove = possibleMoves[moveIdx]
            randAgent.firstMove = firstMove

            worldCopy = copy.deepcopy(world)
            worldCopy.setVerbose(0)

            winner = worldCopy.playThree(randAgent, randAgent2)
            # print('Finished one rollout\n')
            if winner == currentPlayer:
                wins[moveIdx] += 1

        chosenMove = wins.index(max(wins))
        # self.firstMove = None

        return possibleMoves[chosenMove]


    #Returs a wanting boards
    def getBoardMove(self, possibleBoards):
        if len(possibleBoards) == 1:
            return possibleBoards[0]
        else:
            i =random.randint(0,len(possibleBoards)-1)
            return possibleBoards[i]

