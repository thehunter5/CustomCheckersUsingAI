
from succesorFn import findCount
from Terminal_test import hash_state

ts = dict()
def utility(state, start):
    #str1 = hash_state(state)
    #if str1 in ts:
     #   return ts[str1]
    count1 = findCount(state, 1)
    count2 = findCount(state, 2)
    if start == 2:
        diff = count2-count1
    else:
        diff = count1-count2
    #ts[str1] = diff
    return diff
