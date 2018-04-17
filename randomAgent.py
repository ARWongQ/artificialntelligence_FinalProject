import random

#This class holds the information of an agent that behaves randomly
class randomAgent:
    def __init__(self):
        self.name = "Random Agent"

    #Returns a random move between 0-8
    def getMove(self):
        return random.randint(0,8)



