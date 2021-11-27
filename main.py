
from initStateGenerator import *
from succesorFn import *
from Terminal_test import *
from Utility import *
from minimax import *
from alphabeta import *
from PlayGame import *
import datetime

'''

EACH STATE IS DENOTED BY ARRAYLISTOFARRAYLIST HERE BOT'S COLOR IS DENOTED BY 2 AND HUMAN'S COLOR IS DENOTED BY 1 YOU CAN PERFORM MOVES BY
ENTERING ROW NUMBER(0-4 BOTH INCLUSIVE) AND COLUMN NUMBER(STARTING FROM 0 FOR EACH ROW) AND DIRECTION AND TYPE OF MOVE

RANGE OF COLUMN NUMBERS:
0-3 FOR ROWS 0 AND 4
0-4 FOR ROWS 1 AND 3
0-5 FOR ROW 2

THERE ARE SIX DIRECTIONS (0-5 BOTH INCLUSIVE).THEY ARE IN CLOCKWISE ORDER
0- HORIZONTAL LEFT
1- UPPER LEFT
2- UPPER RIGHT
3- HORIZONTAL RIGHT
4- DOWNWARD RIGHT
5- DOWNWARD LEFT

TYPE OF MOVE IS 1(TYPE 1 MOVE) OR 2(TYPE 2 MOVE OR JUMP)

SAMPLE INPUT (IMPORTANT)
****    
        Enter 1 to play first(start the game), 2 to play 2nd:1
        Enter row number in (0,4) both inclusive:0
        Enter col number:1
        Enter an integer in range(0,5) to specify direction:3
        Enter 1 or 2 for type of move:1
****
It will ask at every move that whether you want to end the game or not -Ans YES(i.e. 1) if you want to continue

if you will leave the game in between then there is no gurantee that AI will win**
I have taken depth of minimax to be 3 for speed purposes instead of complete output




'''

def main():
    a = datetime.datetime.now()
    while True:
        option = int(input("Enter 1 for displaying empty board,2 for minimax and 3 for alphabeta and 4 for exit:"))
        if option == 4:
            print("Exiting game.........")
            b = datetime.datetime.now()
            print("Time taken:")
            print(b - a)
            break
        if option == 1:
            eb = [[0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0]]
            displayBoard(eb)
            print("")
        elif option == 2:
            i1 = initStateGenerator()
            print("Displaying the initial state:")
            displayBoard(i1)
            playgame(i1, option)
        elif option == 3:
            i1 = initStateGenerator()
            print("Displaying the initial state:")
            displayBoard(i1)
            print("")
            playgame(i1, option)
        else:
            print("Exiting game.........")
            b = datetime.datetime.now()
            print("Time taken:")
            print(b - a)
            break

main()