import UltimateTTT
import randomAgent

#This class holds the information of an agent that uses rollout
class rolloutAgent:
    def __init__(self):
        self.name = "Rollout Agent"

    #Uses rollout to pick a next move
    def getMove(self, world, possibleMoves, currentPlayer):
        rolloutNum = 1000
        wins = [0] * len(possibleMoves)
        randAgent = randomAgent()

        for i in xrange(rolloutNum):
            moveIdx = i%len(possibleMoves)
            firstMove = possibleMoves[moveIdx]

            winner = world.playThree(randAgent, randAgent, firstMove)

            if winner == currentPlayer:
                wins[moveIdx] += 1

        chosenMove = wins.index(max(wins))

        return chosenMove



