
from Terminal_test import Terminal_test
import copy
from succesorFn import *
from alphabeta import *
from minimax import *

def isanyPossibleMove(state,turn):
    s1 = getSuccesors(state, turn)
    if len(s1) == 0:
        return False
    return True

def playgame(state, algo):
    starter = int(input("Enter 1 to play first(start the game), 2 to play 2nd:"))
    #moves = int(input("Enter maximum number of moves:"))
    choice = 1
    turn = starter
    temp_state = copy.deepcopy(state)
    while isanyPossibleMove(temp_state, turn) and choice == 1:

        if turn == 1:
            count = 5
            flag = 0
            while count > 0:
                rs = int(input("Enter row number in (0,4) both inclusive:"))
                cs = int(input("Enter col number:"))
                direction = int(input("Enter an integer in range(0,5) to specify direction:"))
                mov = int(input("Enter 1 or 2 for type of move:"))
                if rs>=0 and rs <= 4 and cs>=0 and cs<max_col(rs) and state[rs][cs] == turn:
                    #print(state)
                    if isFeasible(state, rs, cs, direction, mov):
                        state = newState(state, rs, cs, direction, mov)
                        displayBoard(state)
                        print("")
                        print("Turn: bot:")
                        turn = 2
                        flag = 1
                        break
                count -= 1
                print("Move not possible. Try some other move")
            if flag == 0:
                print("You have exceeded the time limit !")
                break
            else:
                continue
        else:
            node = Node(2, state, 0, None)
            best_move = None
            if algo == 3:
                best_move = alpha_beta(node, 3, starter)
            else:
                best_move = minimax(node, 3, starter)
            state = copy.deepcopy(best_move.state)
            displayBoard(state)
            print("")
            print("Turn : You :")
            turn = 1
        #moves -= 1
        choice = int(input("Do you want to play further? 0:No 1:Yes"))
        if choice == 0:
            print("Game Over")
            """count1 = findCount(state, 1)
            count2 = findCount(state, 2)
            if count2 > count1:
                print("Sorry ! Seems you lost")
            else:
                print("You won!")"""

def displayBoard(state):
    print(" ", " ", state[0][0], " ", state[0][1], " ", state[0][2], " ", state[0][3], " ")
    print(" ", state[1][0], " ", state[1][1], " ", state[1][2], " ", state[1][3], " ", state[1][4], " ")
    print(state[2][0], " ", state[2][1], " ", state[2][2], " ", state[2][3], "", state[2][4], " ", state[2][5], " ")
    print(" ", state[3][0], " ", state[3][1], " ", state[3][2], " ", state[3][3], " ", state[3][4], " ")
    print(" ", " ", state[4][0], " ", state[4][1], " ", state[4][2], " ", state[4][3], " ", )

"""i1=initStateGenerator()
print(i1)
playgame(i1, 3)
"""