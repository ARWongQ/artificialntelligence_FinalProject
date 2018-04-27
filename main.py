from UltimateTTT import UltimateTTT
from randomAgent import  randomAgent
from rolloutAgent import rolloutAgent
#Main Function
def main():
    print("Running Ultimate Tic Tac Toe")

    myBoard = UltimateTTT()
    rAgent = randomAgent()
    rollAgent = rolloutAgent()

    #myBoard.play()

    myBoard.playThree(rollAgent,rAgent)


#Run the main function
if __name__ == "__main__":
    main()
