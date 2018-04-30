from UltimateTTT import UltimateTTT
from randomAgent import  randomAgent
from rolloutAgent import rolloutAgent
from minimaxAgent import minimaxAgent
#Main Function
def main():
    print("Running Ultimate Tic Tac Toe")

    #myBoard = UltimateTTT()
    rAgent = randomAgent()
    rollAgent = rolloutAgent()
    minmaxAgent = minimaxAgent()

    #myBoard.play()

    numGames = 10
    wins = [0, 0, 0]



    # ROLLOUT AGENT
    """
    for i in xrange(numGames):
        print('Game ' + str(i))
        myBoard.playThree(rollAgent,rAgent)
        if myBoard.wonBy == 'X':
            wins[0] += 1
        elif myBoard.wonBy == 'O':
            wins[1] += 1
        else:
            wins[2] += 1

    print('Rollout Agent won ' + str(wins[0]) + ' times.\nRandom Agent won ' + str(wins[1]) + ' times.\nTied won ' + str(wins[2]) + ' times.\n')
    # myBoard.playTwo(rollAgent)
    """


    # MINIMAX AGENT
    """
    for i in xrange(numGames):
        print('Game ' + str(i))
        myBoard = UltimateTTT()
        myBoard.playFour(minmaxAgent,rAgent)
        if myBoard.wonBy == 'X':
            wins[0] += 1
        elif myBoard.wonBy == 'O':
            wins[1] += 1
        else:
            wins[2] += 1

    print('Minimax Agent won ' + str(wins[0]) + ' times.\nRandom Agent won ' + str(wins[1]) + ' times.\nTied won ' + str(wins[2]) + ' times.\n')
    """

#Run the main function
if __name__ == "__main__":
    main()
