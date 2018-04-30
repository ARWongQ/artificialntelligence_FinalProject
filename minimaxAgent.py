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

        #define types of move. If a board is already won/lost, do not consider Block, Synergy, or Win in eval
        localBlock = 10
        localSynergy = 5
        localWin = 20 #a local win will always also award synergy points
        oppGetsOpenMove = -75
        oppWinsGame = -250
        youWinGame = 500
        oppGetsToWinLocal = -15
        oppGetsToBlock = -20
        oppGetsToBlockGlobal = -60

        bestmove = 0
        poss_moves, poss_states = self.getMoves(state) #poss_states is an UltimateTTT object, not just one TTT object
        move_points = [0]*len(poss_moves)
        bestpoints = 0
        for i, state in enumerate(poss_states):
            # evaluate state
            move_points[i] = 0

            #looking at     UTTT Board     mainboard       Y coord                      Xcoord
            currentBoard = poss_states[i].mainGrid[poss_states[i].current_board[0]][poss_states[i].current_board[1]]

            move_made = possibleMoves[i]
            oppBoard = "" #This should be replaced with an empty TTT board that the following switch will replace
            my_symbol = "" #This WILL be replaced
            their_symbol = "" #This WILL ALSO be replaced
            #This "switch statement" checks local moves (moves that affect the current board)
            if move_made == 0: #top left move
                oppBoard = poss_states[i].mainGrid[0][0]  # this is the board the opponent is sent to by this move
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
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][0].val == my_symbol and currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol and currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[2][2].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergies
                if (currentBoard.grid[1][0].val == my_symbol or currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol or currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[2][2].val == my_symbol):
                    # Synergize!
                    move_points[i] += localSynergy
            elif move_made == 1: #top mid move
                oppBoard = poss_states[i].mainGrid[0][1]  # this is the board the opponent is sent to by this move
                my_symbol = currentBoard.grid[0][1].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[2][1].val == their_symbol) or (
                        currentBoard.grid[0][0].val == their_symbol and currentBoard.grid[0][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[2][1].val == my_symbol) or (
                        currentBoard.grid[0][0].val == my_symbol and currentBoard.grid[0][2].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergies
                if (currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[2][1].val == my_symbol) or (
                        currentBoard.grid[0][0].val == my_symbol or currentBoard.grid[0][2].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 2: #top right move
                oppBoard = poss_states[i].mainGrid[0][2]  # this is the board the opponent is sent to by this move
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
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][2].val == my_symbol and currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol and currentBoard.grid[0][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[2][0].val == my_symbol):
                    # win!
                    move_points[i] += localWin
                #check for local synergies
                if (currentBoard.grid[1][2].val == my_symbol or currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol or currentBoard.grid[0][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[2][0].val == my_symbol):
                    # win!
                    move_points[i] += localSynergy
            elif move_made == 3: #mid left move
                oppBoard = poss_states[i].mainGrid[1][0]  # this is the board the opponent is sent to by this move
                my_symbol = currentBoard.grid[1][0].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[0][0].val == their_symbol and currentBoard.grid[2][0].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[1][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock
                #check for local Win
                if (currentBoard.grid[0][0].val == my_symbol and currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[1][2].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergies
                if (currentBoard.grid[0][0].val == my_symbol or currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[1][2].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 4: #mid mid move
                oppBoard = poss_states[i].mainGrid[1][1]  # this is the board the opponent is sent to by this move
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
                    move_points[i] += localBlock
                #check for Local Win
                if (currentBoard.grid[0][0].val == my_symbol and currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[2][0].val == my_symbol and currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[1][0].val == my_symbol and currentBoard.grid[1][2].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol and currentBoard.grid[2][1].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergy
                if (currentBoard.grid[0][0].val == my_symbol or currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[2][0].val == my_symbol or currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[1][0].val == my_symbol or currentBoard.grid[1][2].val == my_symbol) or (
                        currentBoard.grid[0][1].val == my_symbol or currentBoard.grid[2][1].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 5: #mid right move
                oppBoard = poss_states[i].mainGrid[1][2]  # this is the board the opponent is sent to by this move
                my_symbol = currentBoard.grid[1][2].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[0][2].val == their_symbol and currentBoard.grid[2][2].val == their_symbol) or (
                        currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[1][0].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[0][2].val == my_symbol and currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[1][0].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergy
                if (currentBoard.grid[0][2].val == my_symbol or currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[1][0].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 6: #bot left move
                oppBoard = poss_states[i].mainGrid[2][0]  # this is the board the opponent is sent to by this move
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
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][0].val == my_symbol and currentBoard.grid[0][0].val == my_symbol) or (
                        currentBoard.grid[2][1].val == my_symbol and currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[0][2].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergy
                if (currentBoard.grid[1][0].val == my_symbol or currentBoard.grid[0][0].val == my_symbol) or (
                        currentBoard.grid[2][1].val == my_symbol or currentBoard.grid[2][2].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[0][2].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 7: #bot mid move
                oppBoard = poss_states[i].mainGrid[2][1]  # this is the board the opponent is sent to by this move
                my_symbol = currentBoard.grid[2][1].val
                if my_symbol == 'X':
                    their_symbol = 'O'
                else:
                    their_symbol = 'X'
                # check to see if the move you made blocked the opponent locally
                if (currentBoard.grid[1][1].val == their_symbol and currentBoard.grid[0][1].val == their_symbol) or (
                        currentBoard.grid[2][0].val == their_symbol and currentBoard.grid[2][2].val == their_symbol):
                    # blocked!
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[0][1].val == my_symbol) or (
                        currentBoard.grid[2][0].val == my_symbol and currentBoard.grid[2][2].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                if (currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[0][1].val == my_symbol) or (
                        currentBoard.grid[2][0].val == my_symbol or currentBoard.grid[2][2].val == my_symbol):
                    # Synergy!
                    move_points[i] += localSynergy
            elif move_made == 8: #bot right move
                oppBoard = poss_states[i].mainGrid[2][2]  # this is the board the opponent is sent to by this move
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
                    move_points[i] += localBlock
                #check for local win
                if (currentBoard.grid[1][2].val == my_symbol and currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[2][1].val == my_symbol and currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol and currentBoard.grid[0][0].val == my_symbol):
                    # Win!
                    move_points[i] += localWin
                #check for local synergy
                if (currentBoard.grid[1][2].val == my_symbol or currentBoard.grid[0][2].val == my_symbol) or (
                        currentBoard.grid[2][1].val == my_symbol or currentBoard.grid[2][0].val == my_symbol) or (
                        currentBoard.grid[1][1].val == my_symbol or currentBoard.grid[0][0].val == my_symbol):
                    # Win!
                    move_points[i] += localSynergy

            #check opponent's next move assuming greed (they WILL win the next board or block you if possible)
            oppMovesList = oppBoard.getPossibleMoves()
            if len(oppMovesList) == 0: #opponent was given an open move
                move_points += oppGetsOpenMove

            for k in range (len(oppMovesList)): #go through all possible opponent next moves
                oppMove = oppMovesList[k]
                if oppMove == 0:  # top left move
                    # Check to see if Opponent gets to win a local board
                    if (oppBoard.grid[1][0].val == their_symbol and oppBoard.grid[2][0].val == their_symbol) or (
                            oppBoard.grid[0][1].val == their_symbol and oppBoard.grid[0][2].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[2][2].val == their_symbol):
                        #Opponent wins a board!
                        move_points[i] += oppGetsToWinLocal
                    # check to see if the move they make will block you locally
                    if (oppBoard.grid[1][0].val == my_symbol and oppBoard.grid[2][0].val == my_symbol) or (
                            oppBoard.grid[0][1].val == my_symbol and oppBoard.grid[0][2].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[2][2].val == my_symbol):
                        # Opponent blocks you!
                        move_points[i] += oppGetsToBlock
                elif oppMove == 1:  # top mid move
                    # Opponent can win a board
                    if (oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[2][1].val == their_symbol) or (
                            oppBoard.grid[0][0].val == their_symbol and oppBoard.grid[0][2].val == their_symbol):
                        # blocked!
                        move_points[i] += oppGetsToWinLocal
                    # Opponent can block you
                    if (oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[2][1].val == my_symbol) or (
                            oppBoard.grid[0][0].val == my_symbol and oppBoard.grid[0][2].val == my_symbol):
                        # Win!
                        move_points[i] += oppGetsToBlock
                elif oppMove == 2:  # top right move
                    # Opponent CAN win locally
                    if (oppBoard.grid[1][2].val == their_symbol and oppBoard.grid[2][2].val == their_symbol) or (
                            oppBoard.grid[0][1].val == their_symbol and oppBoard.grid[0][0].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[2][0].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[1][2].val == my_symbol and oppBoard.grid[2][2].val == my_symbol) or (
                            oppBoard.grid[0][1].val == my_symbol and oppBoard.grid[0][0].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[2][0].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 3:  # mid left move
                    # Opponent CAN win locally
                    if (oppBoard.grid[0][0].val == their_symbol and oppBoard.grid[2][0].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[1][2].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[0][0].val == my_symbol and oppBoard.grid[2][0].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[1][2].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 4:  # mid mid move
                    # Opponent CAN win local
                    if (oppBoard.grid[0][0].val == their_symbol and oppBoard.grid[2][2].val == their_symbol) or (
                            oppBoard.grid[2][0].val == their_symbol and oppBoard.grid[0][2].val == their_symbol) or (
                            oppBoard.grid[1][0].val == their_symbol and oppBoard.grid[1][2].val == their_symbol) or (
                            oppBoard.grid[0][1].val == their_symbol and oppBoard.grid[2][1].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[0][0].val == my_symbol and oppBoard.grid[2][2].val == my_symbol) or (
                            oppBoard.grid[2][0].val == my_symbol and oppBoard.grid[0][2].val == my_symbol) or (
                            oppBoard.grid[1][0].val == my_symbol and oppBoard.grid[1][2].val == my_symbol) or (
                            oppBoard.grid[0][1].val == my_symbol and oppBoard.grid[2][1].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 5:  # mid right move
                    # Opponent CAN win local
                    if (oppBoard.grid[0][2].val == their_symbol and oppBoard.grid[2][2].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[1][0].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[0][2].val == my_symbol and oppBoard.grid[2][2].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[1][0].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 6:  # bot left move
                    # Opponent CAN win local
                    if (oppBoard.grid[1][0].val == their_symbol and oppBoard.grid[0][0].val == their_symbol) or (
                            oppBoard.grid[2][1].val == their_symbol and oppBoard.grid[2][2].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[0][2].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[1][0].val == my_symbol and oppBoard.grid[0][0].val == my_symbol) or (
                            oppBoard.grid[2][1].val == my_symbol and oppBoard.grid[2][2].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[0][2].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 7:  # bot mid move
                    # Opponent CAN win local
                    if (oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[0][1].val == their_symbol) or (
                            oppBoard.grid[2][0].val == their_symbol and oppBoard.grid[2][2].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN blcck
                    if (oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[0][1].val == my_symbol) or (
                            oppBoard.grid[2][0].val == my_symbol and oppBoard.grid[2][2].val == my_symbol):
                        move_points[i] += oppGetsToBlock
                elif oppMove == 8:  # bot right move
                    # Opponent CAN win local
                    if (oppBoard.grid[1][2].val == their_symbol and oppBoard.grid[0][2].val == their_symbol) or (
                            oppBoard.grid[2][1].val == their_symbol and oppBoard.grid[2][0].val == their_symbol) or (
                            oppBoard.grid[1][1].val == their_symbol and oppBoard.grid[0][0].val == their_symbol):
                        move_points[i] += oppGetsToWinLocal
                    # Opponent CAN block
                    if (oppBoard.grid[1][2].val == my_symbol and oppBoard.grid[0][2].val == my_symbol) or (
                            oppBoard.grid[2][1].val == my_symbol and oppBoard.grid[2][0].val == my_symbol) or (
                            oppBoard.grid[1][1].val == my_symbol and oppBoard.grid[0][0].val == my_symbol):
                        move_points[i] += oppGetsToBlock


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

