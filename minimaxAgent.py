import random
import UltimateTTT
import copy
from TicTacToe import TicTacToe

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
    def evalBoard(self,state,possibleMoves):

        #define types of move
        localBlock = 10
        localSynergy = 3
        localWin = 20
        oppGetsOpenMove = -75
        oppWinsGame = -250
        youWinGame = 50000000
        oppGetsToBlock = -20
        oppGetsToBlockGlobal = -60

        bestmove = 0
        poss_moves, poss_states = self.getMoves(state) #poss_states is an UltimateTTT object, not just one TTT object
        move_points = [0]*len(poss_moves)
        for i, state in enumerate(poss_states):
            # evaluate state
            move_points[i] = 0
            bestpoints = 0

            #looking at     UTTT Board     mainboard       Y coord                      Xcoord
            currentBoard = poss_states[i].mainGrid[poss_states[i].current_board[0]][poss_states[i].current_board[1]]

            move_made = possibleMoves[i]

            if move_made == 0: #top left move
                my_symbol = currentBoard.grid[0][0].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][0].val == their_symbol and currentBoard.grid[2][0].val == their_symbol) or (
                        currentBoard.grid[0][1].val == their_symbol and currentBoard.grid[0][2].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[2][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 1: #top mid move
                my_symbol = currentBoard.grid[0][1].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[2][1].val == their_symbol) or (
                        currentBoard.grid[0][0].val == their_symbol and currentBoard.grid[0][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 2: #top right move
                my_symbol = currentBoard.grid[0][2].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][2].val == their_symbol and currentBoard.grid[2][2].val == their_symbol) or (
                        currentBoard.grid[0][1].val == their_symbol and currentBoard.grid[0][0].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[2][0].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 3: #mid left move
                my_symbol = currentBoard.grid[1][0].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[0][0].val == their_symbol and currentBoard.grid[2][0].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[1][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 4: #mid mid move
                my_symbol = currentBoard.grid[1][1].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[0][0].val == their_symbol and currentBoard.grid[2][2].val == their_symbol) or (
                        currentBoard.grid[2][0].val == their_symbol and currentBoard.grid[0][2].val == their_symbol) or (
                        currentBoard.grid[1][0].val == their_symbol and currentBoard.grid[1][2].val == their_symbol) or (
                        currentBoard.grid[0][1].val == their_symbol and currentBoard.grid[2][1].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 5: #mid right move
                my_symbol = currentBoard.grid[1][2].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[0][2].val == their_symbol and currentBoard.grid[2][2].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[1][0].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 6: #bot left move
                my_symbol = currentBoard.grid[2][0].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][0].val == their_symbol and currentBoard.grid[0][0].val == their_symbol) or (
                        currentBoard.grid[2][1].val == their_symbol and currentBoard.grid[2][2].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[0][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 7: #bot mid move
                my_symbol = currentBoard.grid[2][1].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[0][1].val == their_symbol) or (
                        currentBoard.grid[2][0].val == their_symbol and currentBoard.grid[2][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;

            elif move_made == 8: #bot right move
                my_symbol = currentBoard.grid[2][2].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][2].val == their_symbol and currentBoard.grid[0][2].val == their_symbol) or (
                        currentBoard.grid[2][1].val == their_symbol and currentBoard.grid[2][0].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[0][0].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock;



            if move_points[i] > bestpoints:
                bestpoints = move_points[i]
                bestmove = poss_moves[i]

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
                min_move = poss_moves[i]
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

