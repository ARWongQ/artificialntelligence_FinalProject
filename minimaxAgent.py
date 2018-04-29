import random
import UltimateTTT
import copy

from randomAgent import randomAgent

#This class holds the information of an agent that uses minimax
class minimaxAgent:
    def __init__(self):
        self.name = "Minimax Agent"
        self.firstMove = None


    # function returns list of possible next states
    def getMoves(self,state):
        states = []
        moves = []
        pass
        return (moves,states)


    # function evaluates current state and chooses best move
    def evalBoard(self,state):
        bestmove = 0
        pass
        return bestmove
    

    # function performs 'min' action - chooses best move of opponent and returns score
    def minEval(self,state):
        min_move = none
        poss_moves, poss_states = self.getMoves(state)
        min_points = 1000000
        for i, state in enumerate(poss_states):
            max_points = self.evalBoard(state)
            if max_points < min_points:
                min_points = max_points
                min_move = i
        return min_move


    # function performs minimax algorithm
    def minimax(self,curr_board):
        poss_moves,poss_states = self.getMoves(curr_Board)
        max_points = -1000000
        best_move = poss_moves[0]
        for i,state in enumerate(poss_states):
            min_points = self.minEval(state)
            if min_points > max_points:
                max_points = min_points
                best_move = i
        return best_move

