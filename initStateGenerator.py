
import math
from random import randint
from tkinter import *

def initStateGenerator():
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
    initial_state = [[0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0]]

    hs = set()
    while len(hs) < 10:
        cell = randint(0, 23)
        if cell not in hs:
            hs.add(cell)
            row = dr[cell]
            col = dc[cell]
            initial_state[row][col] = 1
    while len(hs) < 20:
        cell = randint(0, 23)
        if cell not in hs:
            hs.add(cell)
            row = dr[cell]
            col = dc[cell]
            initial_state[row][col] = 2
    return initial_state


#i1 = initStateGenerator()
#print(i1)