
#import ast
from succesorFn import findCount
from succesorFn import getSuccesors
from succesorFn import max_col
terminal_states=dict()

def hash_state(state):
    str1 = ""
    #k = 0
    for i in range(5):
        col = max_col(i)
        for j in range(col):
            str1 = str1+""+str(state[i][j])
    return str1
def Terminal_test(state):
    str1 = hash_state(state)
    if str1 in terminal_states:
        return True
    count1 = findCount(state, 1)
    count2 = findCount(state, 2)
    if count1 == 0 or count2 == 0:
        terminal_states[str1] = state
        return True
    x1 = getSuccesors(state, 1)
    x2 = getSuccesors(state, 2)
    if len(x1) == 0 and len(x2) == 0:
        terminal_states[str1] = state
        return True
    return False
