
from random import randint
from initStateGenerator import initStateGenerator
import copy
#from Terminal_test import terminal_states
dr = dict()
for i in range(4):
    dr[i] = 0
for i in range(4, 9):
    dr[i] = 1
for i in range(9, 15):
    dr[i] = 2
for i in range(15, 20):
    dr[i] = 3
for i in range(20, 24):
    dr[i] = 4
dc = dict()
dc[0] = 0
dc[4] = 0
dc[9] = 0
dc[15] = 0
dc[20] = 0
dc[1] = 1
dc[5] = 1
dc[10] = 1
dc[16] = 1
dc[21] = 1
dc[2] = 2
dc[6] = 2
dc[11] = 2
dc[17] = 2
dc[22] = 2
dc[3] = 3
dc[7] = 3
dc[12] = 3
dc[18] = 3
dc[23] = 3
dc[8] = 4
dc[13] = 4
dc[19] = 4
dc[14] = 5
def findCount(state,turn):

    count=0
    for i in range(24):
        [row,col]=[dr[i],dc[i]]
        if state[row][col]==turn:
            count+=1
    return count
def findIndices(state,turn):
    hs=set()
    while len(hs)<24:
        cell=randint(0,23)
        if cell in hs:
            continue
        row=dr[cell]
        col=dc[cell]
        if state[row][col]==turn:
            return [row,col]
        hs.add(cell)
def max_col(row):
    m_col = 4
    if row == 1 or row == 3:
        m_col = 5
    elif row == 2:
        m_col = 6
    return m_col
def isFeasible(state,row,col,direction,move):

    if move==1:
        if direction==0:
            if col-1>=0 and state[row][col-1]==0:
                return True
        elif direction==1:
            if row-1>=0 :
                if row<=2 and col-1>=0 and state[row-1][col-1]==0:
                    return True
                elif row>2 and row<=4 and col<max_col(row-1) and state[row-1][col]==0:
                    return True
        elif direction==2:
            if row-1>=0 :
                if row<=2  and col<max_col(row-1) and state[row-1][col]==0:
                    return True
                elif row>2 and row<=4 and col+1<max_col(row-1) and state[row-1][col+1]==0:
                    return True
        elif direction==3:
            if col+1<max_col(row)  and state[row][col+1]==0:
                return True
        elif direction==4:
            if row+1<=4 :
                if row<2 and col+1<max_col(row+1) and state[row+1][col+1]==0:
                    return True
                elif row>=2  and col<max_col(row+1) and state[row+1][col]==0:
                    return True
        elif direction==5:
            if row+1<=4  :
                if row<2 and state[row+1][col]==0:
                    return True
                elif row>=2 and row<=4 and col-1>=0 and state[row+1][col-1]==0:
                    return True
    else:
        if direction==0:
            if col-2>=0 and state[row][col-2]==0 and state[row][col-1]!=state[row][col] and state[row][col-1]!=0:
                return True
        elif direction == 1:
            if row-2>=0 and col+row-4>=0 and col+row-4<max_col(row-2) and state[row-2][col+row-4]==0 :
                if row==2 and state[row-1][col-1]!=state[row][col] and state[row-1][col-1]!=0:
                    return True
                elif row>2 and row<=4 and state[row-1][col]!=state[row][col] and state[row-1][col]!=0:
                    return True
        elif direction==2:
            if row-2>=0 and col+row-2<max_col(row-2) and col+row-2>=0 and state[row-2][col+row-2]==0:
                if row==2 and col<max_col(row-1) and state[row-1][col]!=state[row][col] and state[row-1][col]!=0:
                    return True
                elif row>2 and row<=4 and col+1<max_col(row-1) and state[row-1][col+1]!=state[row][col] and state[row-1][col+1]!=0:
                    return True
        elif direction==3:
            if col+2<max_col(row) and state[row][col+2]==0 and state[row][col+1]!=state[row][col] and state[row][col+1]!=0:
                return True
        elif direction==4:
            if row+2<=4 and col+2-row>=0 and col+2-row<max_col(row+2) and state[row+2][col+2-row]==0:
                if row==2 and state[row][col]!=state[row+1][col] and state[row+1][col]!=0:
                    return True
                elif row>=0 and row<2 and state[row+1][col+1]!=state[row][col] and state[row+1][col+1]!=0:
                    return True
        elif direction==5:
            if row+2<=4 and col-row>=0 and col-row<max_col(row+2) and state[row+2][col-row]==0:
                if row==2 and state[row][col]!=state[row+1][col-1] and state[row+1][col-1]!=0:
                    return True
                elif row>=0 and row<2 and state[row][col]!=state[row+1][col] and state[row+1][col]!=0:
                    return True
    return False
def newState(state1,row,col,direction,move):
    #state=list(state1)
    if move==1:
        if direction==0:
            state1[row][col-1]=state1[row][col]
            state1[row][col]=0
            return state1
        elif direction==1:
            if row<=2:
                state1[row - 1][col - 1] = state1[row][col]
                state1[row][col] = 0
                return state1
            else:
                state1[row - 1][col] = state1[row][col]
                state1[row][col] = 0
                return state1
        elif direction==2:
            if row<=2:
                state1[row - 1][col] = state1[row][col]
                state1[row][col] = 0
                return state1
            else:
                state1[row - 1][col+1] = state1[row][col]
                state1[row][col] = 0
                return state1
        elif direction==3:
            state1[row][col+1]=state1[row][col]
            state1[row][col] = 0
            return state1
        elif direction==4:
            if row<2:
                state1[row + 1][col+1] = state1[row][col]
                state1[row][col] = 0
                return state1
            else:
                state1[row +1][col] = state1[row][col]
                state1[row][col] = 0
                return state1
        else:
            if row<2:
                state1[row + 1][col] = state1[row][col]
                state1[row][col] = 0
                return state1
            else:
                state1[row +1][col-1] = state1[row][col]
                state1[row][col] = 0
                return state1
    else:
        if direction==0:
            state1[row][col-2]=state1[row][col]
            state1[row][col] = 0
            state1[row][col-1]=0
            return state1
        elif direction==1:
            state1[row-2][col+row-4]=state1[row][col]
            if row == 2 :
                state1[row - 1][col - 1]=0
            else:
                state1[row - 1][col]=0
            state1[row][col]=0
            return state1
        elif direction==2:
            state1[row - 2][col + row - 2] =state1[row][col]
            if row == 2 :
                state1[row - 1][col]=0
            else:
                state1[row - 1][col+1]=0
            state1[row][col]=0
            return state1
        elif direction==3:
            state1[row][col + 2] =state1[row][col]
            state1[row][col+1]=0
            state1[row][col] = 0
            return state1
        elif direction==4:
            state1[row + 2][col + 2 - row]=state1[row][col]
            if row==2:
                state1[row+1][col]=0
            else:
                state1[row+1][col+1]=0
            state1[row][col] = 0
            return state1
        else:
            state1[row + 2][col - row] =state1[row][col]
            if row==2:
                state1[row+1][col-1]=0
            else:
                state1[row+1][col]=0
            state1[row][col] = 0
            return state1
def succesorFn(state,turn):
    #if turn==2:
        count=findCount(state,turn)
        if count>0:
            trials=count
            locations=set()
            while trials>0:
                [row,col]=findIndices(state,turn)
                p1 = (row, col)
                if (p1 in locations):
                    continue
                movs=set()
                while len(movs)<12:
                    direction=randint(0,5)
                    move=randint(1,2)
                    p=(direction,move)
                    if p in movs:
                        continue
                    if isFeasible(state,row,col,direction,move):
                        print(state)
                        state1=copy.deepcopy(state)
                        s= newState(state1,row,col,direction,move)
                        print(state)
                        return s

                    movs.add(p)

                locations.add(p1)
                trials=trials-1
            #we will call succesor function only if current state is non terminal
def getSuccesors(state,turn):
    count = findCount(state, turn)
    next_States = []
    if count==0:
        return next_States
    else:

        trials = count
        locations = set()
        while trials > 0:
            [row, col] = findIndices(state, turn)
            p1 = (row, col)
            if (p1 in locations):
                continue
            movs = set()
            while len(movs) < 12:
                direction = randint(0, 5)
                move = randint(1, 2)
                p = ""+str(direction)+str(move)
                if p in movs:
                    continue
                if move==1:
                    #p2=(direction,2)
                    if isFeasible(state, row, col, direction, 2):
                        movs.add(p)
                        continue
                if isFeasible(state, row, col, direction, move):
                    state1=copy.deepcopy(state)
                    s= newState(state1, row, col, direction, move)
                    #print(list(s))
                    next_States.append(s)

                movs.add(p)

            locations.add(p1)
            trials = trials - 1
        return next_States
"""i1=initStateGenerator()
print(i1)
#i1=[[2,1,2,1],[1,2,0,1,0],[1,2,1,1,1,2],[1,1,2,2,2],[2,0,0,2]]
#i2=list(i1)
#print(i1)
#print(i2)


#i1=[[2,1,2,1],[1,2,0,1,0],[1,2,1,1,1,2],[1,1,2,2,2],[2,0,0,2]]
n_state=getSuccesors(i1,1)
print(len(n_state))
for i in range(len(n_state)):
    print(n_state[i])
"""