from UltimateTTT import UltimateTTT
from randomAgent import  randomAgent
#Main Function
def main():
    print("Running Ultimate Tic Tac Toe")

    myBoard = UltimateTTT()
    rAgent = randomAgent()

    #myBoard.play()

    myBoard.playThree(rAgent,rAgent,None)


#Run the main function
if __name__ == "__main__":
    main()
